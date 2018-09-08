score = 0

def add(value):
    global score
    score = score + value

def get():
    return score

def empty():
    global score
    score = 0