from state import circle_storage
from state import button_storage
from state import score_storage
import cv2
import math

font_color = (105, 100, 230)
font_type = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_weight = 2
font_line = cv2.LINE_AA

def draw(image):
    #renderCircle(image, "button")
    renderCircle(image, "15")
    renderCircle(image, "10")
    renderCircle(image, "5")
    renderButton(image, "button", "0")
    renderScore(image)

    circle_storage.empty()
    button_storage.empty()
    score_storage.empty()

def renderCircle(image, identifier):
    if circle_storage.get(identifier) is not None:
        x, y, radius, color = circle_storage.get(identifier)
        cv2.circle(image, (x, y), radius, color, 4)

def renderButton(image, identifier, text):
    if button_storage.get() is not None:
        for (x, y, radius, color) in button_storage.buttons:
            if _checkPoints("15", x, y, radius):
                score_storage.add(15)
                renderText(image, "15", (x, y))
            elif _checkPoints("10", x, y, radius):
                score_storage.add(10)
                renderText(image, "10", (x, y))
            elif _checkPoints("5", x, y, radius):
                score_storage.add(5)
                renderText(image, "5", (x, y))
            else:
                renderText(image, text, (x, y))

def _checkPoints(identifier, buttonX, buttonY, buttonR):
    circleX, circleY, circleR, color = circle_storage.get(identifier)
    sideX = math.fabs(circleX - buttonX)
    sideY = math.fabs(circleY - buttonY)
    hypotenuse = _calculate_hypotenuse(sideX, sideY)
    return hypotenuse < (circleR - buttonR)

def _calculate_hypotenuse(sideX, sideY):
    pow = math.pow(sideX, 2) + math.pow(sideY, 2)
    return round(math.sqrt(pow), 3)


def renderScore(image):
    score_text = f"Total score of:{score_storage.get()}"
    renderText(image, score_text, (20, 20), (255, 255, 255))

def renderText(image, text, coordinates, color=font_color):
    cv2.putText(image, text, coordinates, font_type, font_scale, color, font_weight, font_line)