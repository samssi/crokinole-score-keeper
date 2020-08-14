from detect import detect_objects as detect
from render import draw
import cv2

frame_limit = 0

cap = cv2.VideoCapture('rtsp://admin:123456@192.168.10.2/live/ch0')

frame_nbr = 0


def start():
    while True:
        global frame_nbr
        frame_nbr = frame_nbr + 1

        grabbed, frame = cap.read()

        if grabbed:
            detect.detectCircles(frame)
            draw.draw(frame)
            cv2.imshow("frame", frame)

            frame_nbr = 0

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()
