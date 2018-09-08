from state import circle_storage
from state import button_storage
import cv2

font_color = (105, 100, 230)
font_type = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_weight = 2
font_line = cv2.LINE_AA

def draw(image):
    renderButton(image, "button", "0")
    #renderCircle(image, "button")
    renderCircle(image, "15")
    renderCircle(image, "10")
    renderCircle(image, "5")

    circle_storage.empty()
    button_storage.empty()

def renderCircle(image, identifier):
    if circle_storage.get(identifier) is not None:
        x, y, radius, color = circle_storage.get(identifier)
        cv2.circle(image, (x, y), radius, color, 4)

def renderButton(image, identifier, text):
    if button_storage.get() is not None:
        for (x, y, radius, color) in button_storage.buttons:
            cv2.putText(image, text, (x, y), font_type, font_scale, font_color, font_weight, font_line)