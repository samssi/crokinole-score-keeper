from detect import detect_objects as detect
from render import draw
import cv2

frame_limit = 0

cap = cv2.VideoCapture('crok.mp4')

import numpy

#cap.set(cv2.CAP_PROP_FPS, 1)

#fourcc = cv2.VideoWriter_fourcc(*'X264')
#out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))


#while (cap.isOpened()):

frame_nbr = 0

def start():
        while True:
            global frame_nbr
            frame_nbr = frame_nbr + 1

            _, frame = cap.read()

            if frame_nbr > frame_limit:
                detect.detectCircles(frame)
                draw.draw(frame)
                cv2.imshow("frame", frame)

                frame_nbr = 0

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.waitKey(0)
        cv2.destroyAllWindows()
