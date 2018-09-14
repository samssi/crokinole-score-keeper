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
check_20_variance = 5

def draw(image):
    renderCircle(image, "15")
    renderCircle(image, "10")
    renderCircle(image, "5")
    renderButton(image)
    renderScore(image)

    circle_storage.empty()
    button_storage.empty()
    score_storage.empty()

def renderCircle(image, identifier):
    if circle_storage.get(identifier) is not None:
        x, y, radius, color = circle_storage.get(identifier)
        cv2.circle(image, (x, y), radius, color, 4)

def renderButton(image):
    if button_storage.get() is not None:
        for (x, y, radius, color) in button_storage.buttons:
            _button(x, y, radius, image)

def _button(x, y, radius, image):
    color = _sample_color(x, y, radius, image)
    if color is "unknown":
        pass
    elif _check20(x, y, radius):
        score_storage.add(20, color)
        renderText(image, f"20: {color}", (x, y))
    elif _checkPoints("15", x, y, radius):
        score_storage.add(15, color)
        renderText(image, f"15: {color}", (x, y))
    elif _checkPoints("10", x, y, radius):
        score_storage.add(10, color)
        renderText(image, f"10: {color}", (x, y))
    elif _checkPoints("5", x, y, radius):
        score_storage.add(5, color)
        renderText(image, f"5: {color}", (x, y))
    else:
        renderText(image, f"0: {color}", (x, y))

def _sample_color(y, x, radius, image):
    if _sample_for_black(x, y, radius, image):
        return "black"
    elif _sample_for_blue(x, y , radius, image):
        return "blue"
    else:
        return "unknown"

def _sample_for_black(x, y, radius, image):
    for i in range(13):
        b, g, r = image[x + radius - i, y]
        if (0 < r < 105) and (0 < g < 80) and (0 < b < 35):
            return True
    return False

def _sample_for_blue(x, y, radius, image):
    for i in range(30):
        b, g, r = image[x + radius - i, y]
        if (0 < r < 104) and (50 < g < 204) and (1 < b < 255):
            return True
    return False

def _check20(buttonX, buttonY, buttonR):
    circleX, circleY, circleR, color = circle_storage.get("15")
    xDiff = math.fabs(circleX - buttonX)
    yDiff = math.fabs(circleY - buttonY)
    return (xDiff < check_20_variance) and (yDiff < check_20_variance)

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
    score_text = f"Total score of: {score_storage.score}"
    team1_score_text = f"Team 1, score of: {score_storage.team1_score}"
    team2_score_text = f"Team 2. score of: {score_storage.team2_score}"
    renderText(image, score_text, (20, 20), (255, 255, 255))
    renderText(image, team1_score_text, (20, 45), (255, 0, 0))
    renderText(image, team2_score_text, (20, 70), (0, 0, 0))

def renderText(image, text, coordinates, color=font_color):
    cv2.putText(image, text, coordinates, font_type, font_scale, color, font_weight, font_line)