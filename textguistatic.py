import curses as cs
from curses import init_color
from curses import init_pair


class TGStatic:
    C_WHITE = 0  # colors
    C_BLACK = 1
    C_RED = 2
    C_BLUE = 3
    C_GREEN = 4
    C_PINK = 5
    C_YELLOW = 6
    C_GRAY = 7
    C_LIGHT_GRAY = 8
    C_LIGHT_BLUE = 9
    C_LIGHT_PURPLE = 10
    C_MINT = 11
    C_ORANGE = 12
    C_LIGHT_RED = 13
    C_LIME = 14
    C_PURPLE = 15
    P_LIGHT_GRAY_X2 = 10
    P_ORANGE_BLACK = 11
    P_RED_BLACK = 12

    def __init__(self):
        init_color(0, 255, 255, 255)
        init_color(1, 255, 0, 0)
        init_color(2, 0, 0, 0)
        init_color(3, 0, 0, 255)
        init_color(4, 0, 255, 0)
        init_color(5, 255, 0, 255)
        init_color(6, 255, 255, 0)
        init_color(7, 128, 128, 128)
        init_color(8, 192, 192, 192)
        init_color(9, 51, 153, 255)
        init_color(10, 153, 153, 255)
        init_color(11, 102, 255, 178)
        init_color(12, 255, 128, 0)
        init_color(13, 255, 102, 102)
        init_color(14, 153, 255, 51)
        init_color(15, 127, 0, 255)
        init_pair(10, self.C_LIGHT_GRAY, self.C_LIGHT_GRAY)
        init_pair(11, self.C_ORANGE, self.C_BLACK)
