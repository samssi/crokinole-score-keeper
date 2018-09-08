from state import circle_storage
from state import button_storage
from state import score_storage
import cv2

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
            # TODO: polar coordinates of points circles
            if (x > 500 and y > 500) and (x < 900 and y < 900):
                score_storage.add(15)
                renderText(image, "15", (x, y))
            else:
                renderText(image, text, (x, y))

def renderScore(image):
    score_text = f"Total score of:{score_storage.get()}"
    renderText(image, score_text, (20, 20), (255, 255, 255))

def renderText(image, text, coordinates, color=font_color):
    cv2.putText(image, text, coordinates, font_type, font_scale, color, font_weight, font_line)