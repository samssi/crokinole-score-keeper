from state import circle_storage
from state import button_storage
import cv2
import numpy

def storeCircles(image, identifier, circles, r, g, b):
    color = (b, g, r)

    if circles is not None:
        circles = numpy.round(circles[0, :]).astype("int")

        for (x, y, radius) in circles:
            storeCircle(identifier, x, y, radius, color)


def storeCircle(identifier, x, y, radius, color):
    if identifier is "button":
        button_storage.add((x, y, radius, color))
    else:
        circle_storage.put(identifier, (x, y, radius, color))