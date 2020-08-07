score = 0
blue_score = 0
black_score = 0
team_1_color = "blue"
team_2_color = "black"


def add(value, color):
    global score
    score = score + value
    if color is team_1_color:
        add_blue(value)
    else:
        add_black(value)


def add_blue(value):
    global blue_score
    blue_score = (blue_score + value)


def add_black(value):
    global black_score
    black_score = (black_score + value)


def empty():
    global score, blue_score, black_score
    score = 0
    blue_score = 0
    black_score = 0
