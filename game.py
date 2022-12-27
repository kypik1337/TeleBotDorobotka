import aiogram

 
game = False
max_total = 150
total = max_total

def get_total():
    global total
    return total

def take_candis(take: int):
    global total
    total -= take

def new_game():
    global game
    global total
    if game:
        game = False
    else:
        total = max_total
        game = True

def set_max_total(value: int):
    global max_total
    max_total = value

def check_game():
    global game
    return game