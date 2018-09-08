buttons = []

def add(tuple):
    buttons.append(tuple)

def get():
    return buttons

def empty():
    global buttons
    buttons = []