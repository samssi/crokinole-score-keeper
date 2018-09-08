from detect import detect_objects as detect
import cv2

def start():
    image = cv2.imread('crok.jpg')

    detect.detectCircles(image)

    cv2.imshow('result', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()