import cv2
import numpy as np

def HAAR(image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  cascade = cv2.CascadeClassifier("detectors/h1.xml")
  rects = cascade.detectMultiScale(image, scaleFactor=1.1,
                                     minNeighbors=5, minSize=(30, 30),
                                     flags = cv2.CASCADE_SCALE_IMAGE)
                     
  if len(rects) == 0: return []
  rects[:,2:] += rects[:,:2]
  box = []
  for x1, y1, x2, y2 in rects:
     box.append((x1, y1, x2-x1, y2-y1))
  return box

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def HOG(image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  hog = cv2.HOGDescriptor()
  hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector())
  found, w = hog.detectMultiScale(image, winStride=(8,8), padding=(16,16), scale=1.1)
  found_filtered = []
  for ri, r in enumerate(found):
        for qi, q in enumerate(found):
          if ri != qi and inside(r, q): break
          else: found_filtered.append(r)
  box = []
  for x1, y1, w, h in found:
    box.append((x1, y1, w, h))
  return box

def NN(image, H, W, cl='person'):
  CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
  net = cv2.dnn.readNetFromCaffe("detectors/1.prototxt", "detectors/1.caffemodel")
  blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)
  net.setInput(blob)
  detections = net.forward()
  box = []
  for i in range(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.2:
      idx = int(detections[0, 0, i, 1])
      if CLASSES[idx] != cl:
        continue
      b = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
      box.append((int(b[0]), int(b[1]), int(b[2]-b[0]), int(b[3]-b[1])))
  return box
