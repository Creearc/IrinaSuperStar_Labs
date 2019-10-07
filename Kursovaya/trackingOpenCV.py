import argparse
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
                help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="kcf",
                help="OpenCV object tracker type")
args = vars(ap.parse_args())

# extract the OpenCV version info
(major, minor) = cv2.__version__.split(".")[:2]

#  функция для создания трекинга
if int(major) == 3 and int(minor) < 3:
    tracker = cv2.Tracker_create(args["tracker"].upper())

else:
    # инициализируем словарь, который отображает строки в соответствующие им
    # реализация трекера объектов OpenCV
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        "boosting": cv2.TrackerBoosting_create,
        "mil": cv2.TrackerMIL_create,
        "tld": cv2.TrackerTLD_create,
        "medianflow": cv2.TrackerMedianFlow_create,
        "mosse": cv2.TrackerMOSSE_create
    }

    # выберете соответствующий трекер, используя словарь объектов OpenCV
    tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()

#  инициализация координат ограничивающего прямоугольника, который мы будем отслеживать
initBB = None

# если не прописан путь к видео используется веб камера
if not args.get("video", False):
    print("[INFO] starting video stream...")
    vs = VideoStream(src="./drone.mp4").start()

else:
    vs = cv2.VideoCapture(args["video"])

# инициализация оценки пропускной способности FPS
fps = None

# зацикливание видеопотока
while True:
    # захватит текущего кадра, а затем обработка
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame

    # проверка закончилось ли видео
    if frame is None:
        break

    # изменить размер кадра
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    # проверить отслеживаем ли мы объект в данный момент
    if initBB is not None:
        # захватить объект заново
        (success, box) = tracker.update(frame)

        # проверить было ли отслеживание успешным
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x + w, y + h),
                          (0, 255, 0), 2)

        # обновить счетчик FPS
        fps.update()
        fps.stop()

        # инициализирование набор информации, которую будет отображена в кадре
        info = [
            ("Tracker", args["tracker"]),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]

        # перебор информационных кортежей и отрисовка их на кадре
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # показать результирующий кадр
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # при нажатии на клавишу 's', мы собираемся "выбрать" ограничивающую рамку для отслеживания
    if key == ord("s"):
        # выберите область, который мы хотим отслеживать (убедитесь, что вы нажали ENTER
        # ли SPACE после выбора области интереса)
        initBB = cv2.selectROI("Frame", frame, fromCenter=False,
                               showCrosshair=True)

        tracker.init(frame, initBB)
        fps = FPS().start()

    # выйти из цикла если была нажата клавиша `q`
    elif key == ord("q"):
        break

# отпустите указатель если мы используем веб-камеру
if not args.get("video", False):
    vs.stop()

# иначе освободить указатель
else:
    vs.release()

# закрыть все
cv2.destroyAllWindows()

