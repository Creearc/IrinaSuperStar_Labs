import argparse
import math
import cv2
import numpy as np
from detectors.detectors import analyze
from csv_functions import save_coords, clear_paths

W, H = 1270, 720

WAIT = 1

def getind(cur, old):
    position = cur
    l = -1
    x1, y1 = cur[0], cur[1]
    ind = -1
    for i in range(len(old)):
        x0, y0 = old[i][0], old[i][1]
        ln = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        if (l == -1 or l > ln) and ln < 150.0:
            l = ln
            ind = i
    return ind
        
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True)
ap.add_argument("-m", "--method", default = "NN")
ap.add_argument("-c", "--class", default = "person")
args = vars(ap.parse_args())


trackers = cv2.MultiTracker()
cam = cv2.VideoCapture(args["video"])

i = 0

#F = 28.0 * 102 / 1.7
#F = 1680.0
F = 5.5 * 300 / 1.75 # Tur
alpha = 125.0 * 3.14 / 180
Hc = 3.0
Hch = 1.75

D = lambda x:  - math.tan(alpha - math.atan((H / 2 - x) / F)) * Hc
Dx = lambda x, d, y: (W / 2 -x) * ((Hc ** 2 + d ** 2) / ((H / 2 - y) ** 2 + F ** 2)) ** 0.5 

boxes = []
lifes = []
LIFETIME = 10

clear_paths()

while True: 
    ret, frame = cam.read()
    if frame is None: break
    frame = cv2.resize(frame, (W, H))
    if i % 20 == 0:
        trackers = cv2.MultiTracker()
        old_pos = list()
        for box in boxes: old_pos.append((box[0], box[1], box[2], box[3]))
        
        boxes = analyze(frame, args["method"], W, H, args["class"])
        
        pos_temp = old_pos.copy()
        if len(old_pos) > 0:
            for p in range(len(boxes)):
                ind = getind(boxes[p], old_pos)
                if ind != -1:
                    pos_temp[ind] = boxes[p]
                else:
                    lifes.append(LIFETIME)
                    pos_temp.append(boxes[p])
                cv2.putText(frame, str(ind), (int(boxes[p][0]), int(boxes[p][1]) - 20),
                            cv2.FONT_ITALIC, 0.5, (0, 0, 250), 2)
            for p in range(len(old_pos)):
                if p > len(pos_temp) - 1:
                    break 
                if old_pos[p] == pos_temp[p]:
                    if lifes[p] < 1:
                        del pos_temp[p]
                    else:
                        lifes[p] -= 1
                else:
                    lifes[p] = LIFETIME
            boxes = pos_temp.copy()
        else:
            for p in range(len(boxes)):
                lifes.append(LIFETIME)
                
        for box in boxes:
            tracker = cv2.TrackerMOSSE_create()
            trackers.add(tracker, frame, box)           

    else:
        (success, boxes) = trackers.update(frame)

    ind = 0
    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        
        py = D(h + y)
        px = Dx(x + w / 2, py, h + y)
        save_coords(ind, (str(px)[:5], str(py)[:5], 0.0))

        cv2.putText(frame, str(ind), (x, y - 20), cv2.FONT_ITALIC, 0.5, (0, 0, 250), 2)
        cv2.putText(frame, str(px)[:5], (x, y), cv2.FONT_ITALIC, 0.5, (0, 0, 250), 2)
        cv2.putText(frame, str(py)[:5], (x, y + 20), cv2.FONT_ITALIC, 0.5, (0, 0, 250), 2)

        ind += 1
 
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(WAIT) & 0xFF
    if key == ord('q') or key == 27:
        break
    i += 1

cv2.destroyAllWindows()
cam.release()

import show_paths
