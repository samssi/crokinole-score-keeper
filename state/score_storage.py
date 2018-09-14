score = 0
team1_score = 0
team2_score = 0
team_1_color = "blue"
team_2_color = "black"

def add(value, color):
    global score
    score = score + value
    if color is team_1_color:
        add_team1(value)
    else:
        add_team2(value)

def add_team1(value):
    global team1_score
    team1_score = (team1_score + value)

def add_team2(value):
    global team2_score
    team2_score = (team2_score + value)

def empty():
    global score, team1_score, team2_score
    score = 0
    team1_score = 0
    team2_score = 0