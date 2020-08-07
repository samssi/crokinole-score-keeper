from state import circle_storage
from state import button_storage
from state import score_storage
import cv2
import math

default_font_color = (105, 100, 230)
font_type = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_weight = 2
font_line = cv2.LINE_AA
check_20_variance = 5

# BGR colors
white = (255, 255, 255)
blue = (255, 0, 0)
black = (0, 0, 0)


def draw(image):
    render_circle(image, "15")
    render_circle(image, "10")
    render_circle(image, "5")
    render_button(image)
    render_score(image)

    circle_storage.empty()
    button_storage.empty()
    score_storage.empty()


def render_circle(image, identifier):
    if circle_storage.get(identifier) is not None:
        x, y, radius, color = circle_storage.get(identifier)
        cv2.circle(image, (x, y), radius, color, 4)


def render_button(image):
    if button_storage.get() is not None:
        for (x, y, radius, color) in button_storage.buttons:
            _button(x, y, radius, image)


def _button(x, y, radius, image):
    color = _sample_color(x, y, radius, image)
    if color is "unknown":
        pass
    elif _check20(x, y, radius):
        score_storage.add(20, color)
        render_text(image, f"20: {color}", (x, y))
    elif _check_points("15", x, y, radius):
        score_storage.add(15, color)
        render_text(image, f"15: {color}", (x, y))
    elif _check_points("10", x, y, radius):
        score_storage.add(10, color)
        render_text(image, f"10: {color}", (x, y))
    elif _check_points("5", x, y, radius):
        score_storage.add(5, color)
        render_text(image, f"5: {color}", (x, y))
    else:
        render_text(image, f"0: {color}", (x, y))


def _sample_color(y, x, radius, image):
    if _sample_for_black(x, y, radius, image):
        return "black"
    elif _sample_for_blue(x, y, radius, image):
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


def _check_points(identifier, buttonX, buttonY, buttonR):
    circleX, circleY, circleR, color = circle_storage.get(identifier)
    sideX = math.fabs(circleX - buttonX)
    sideY = math.fabs(circleY - buttonY)
    hypotenuse = _calculate_hypotenuse(sideX, sideY)
    return hypotenuse < (circleR - buttonR)


def _calculate_hypotenuse(sideX, sideY):
    pow = math.pow(sideX, 2) + math.pow(sideY, 2)
    return round(math.sqrt(pow), 3)


def _leader_and_score(score_storage):
    tie_label = 'Tied'
    blue_team_lead_label = 'Blue team leads by:'
    black_team_lead_label = 'Black team leads by:'
    score_difference = abs(score_storage.blue_score - score_storage.black_score)
    if score_storage.blue_score > score_storage.black_score:
        return f"{blue_team_lead_label} {score_difference}", blue
    elif score_storage.blue_score < score_storage.black_score:
        return f"{black_team_lead_label} {score_difference}", black
    else:
        return tie_label, white


def render_score(image):
    score_text = f"Total score of: {score_storage.score}"
    blue_team_score_text = f"Team 1, score of: {score_storage.blue_score}"
    black_team_score_text = f"Team 2. score of: {score_storage.black_score}"
    leader_text, leader_color = _leader_and_score(score_storage)
    render_text(image, score_text, (20, 20), white)
    render_text(image, blue_team_score_text, (20, 45), blue)
    render_text(image, black_team_score_text, (20, 70), black)
    render_text(image, leader_text, (20, 95), leader_color)


def render_text(image, text, coordinates, color=default_font_color):
    cv2.putText(image, text, coordinates, font_type, font_scale, color,
                font_weight, font_line)
