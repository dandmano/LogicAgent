import curses as cs
from textguistatic import TGStatic as TGS
from curses import init_color
from curses import init_pair



class TGui:
    TER_LINES = 15
    TER_COLS = 37

    C_WHITE = 10  # colors
    C_BLACK = 30
    C_RED = 12
    C_BLUE = 13
    C_GREEN = 14
    C_PINK = 15
    C_YELLOW = 16
    C_GRAY = 17
    C_LIGHT_GRAY = 35
    C_LIGHT_BLUE = 19
    C_LIGHT_PURPLE = 20
    C_MINT = 21
    C_ORANGE = 22
    C_LIGHT_RED = 23
    C_LIME = 24
    C_PURPLE = 25
    P_LIGHT_GRAY_X2 = 25
    P_ORANGE_BLACK = 16
    P_RED_BLACK = 17
    CH_BLANK_SQUARE = '\U00002800'

    def __init__(self, stdscr):
        self.stdscr = stdscr
        cs.start_color()
        cs.use_default_colors()
        self.stdscr.encoding = "utf-8"
        cs.resize_term(self.TER_LINES, self.TER_COLS)
        self._temp()

    def _temp(self):
        init_color(30, 0, 0, 0)
        init_color(35, 80, 50, 255)
        init_color(22, 0, 0, 255)
        init_pair(25, self.C_LIGHT_GRAY, self.C_LIGHT_GRAY)
        init_pair(16, self.C_ORANGE, self.C_BLACK)

    def __init_menu_window(self):
        self.menu_win = cs.newwin(self.TER_LINES, self.TER_COLS, 0, 0)
        self.menu_win.attrset(cs.color_pair(self.P_LIGHT_GRAY_X2))
        self.menu_win.box('|', '-')
        message = "☺☺Witaj w grze!☺☺"
        self.menu_win.attrset(cs.A_NORMAL)
        self.menu_win.attrset(cs.A_BOLD)
        self.menu_win.addstr(4, int((self.TER_COLS - len(message))/2), message, cs.color_pair(self.P_ORANGE_BLACK))
        self.menu_win.addstr(5, int((self.TER_COLS - len(message))/2), "▲▶▼◀", cs.color_pair(self.P_ORANGE_BLACK)|cs.A_REVERSE)


    def display_menu(self):
        self.__init_menu_window()
        self.menu_win.refresh()

