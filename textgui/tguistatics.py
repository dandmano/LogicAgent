TER_LINES = 20
TER_COLS = 55

WHITE = 0
BLACK = 3
BLUE = 22
GREEN = 47
PURPLE = 58
RED = 197
YELLOW = 227
ORANGE = 203
MAGENTA = 202
LIME = 155
CYAN = 52
LIGHT_BLUE = 28

P_LEFT = '◀'
P_RIGHT = '▶'
P_UP = '▲'
P_DOWN = '▼'
WALL = '■'
CROSSWALL = '▧'
STAR = '✦'
BLANK = '⠀'


def center_x(cols, word):
    return (cols - len(word))//2
