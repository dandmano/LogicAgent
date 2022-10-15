import curses as cs
from textgui.windows import MenuWindow, GameWindow
from textgui.tguistatics import *


class TGui:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.nodelay(True)
        self.stdscr.encoding = "utf-8"
        self.__init_colors()
        cs.curs_set(0)
        cs.resize_term(TER_LINES, TER_COLS)
        stdscr.refresh()
        self._init_menu()

    @property
    def menu(self):
        return self._menu_gui

    @staticmethod
    def __init_colors():
        cs.start_color()
        cs.use_default_colors()
        for i in range(0, 255):
            cs.init_pair(i + 1, i, -1)

    def _init_menu(self):
        self._menu_win = cs.newwin(TER_LINES, TER_COLS, 0, 0)
        self._menu_gui = MenuWindow(self._menu_win, TER_LINES, TER_COLS)

    def _init_game_map(self, level):
        self._game_win = cs.newwin(TER_LINES, TER_COLS, 0, 0)
        self._level_win = cs.newwin(13, 21, 2, 17)
        self._game_gui = GameWindow(self._game_win, self._level_win, TER_LINES, TER_COLS, level)

    def new_game(self, level):
        self._init_game_map(level)
        return self._game_gui

    def getkey(self):
        return self.stdscr.getkey()


