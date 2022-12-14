import curses as cs

from pygame import init

from textgui.tguistatics import *
from textgui.windows import MenuWindow, GameWindow


#  Glowna klasa interfejsu graficznego. Inicjalizuje interfejs (curses), jego okna i podokna oraz kolory
class TGui:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.is_graphic = False
        self.stdscr.nodelay(True)
        self.stdscr.encoding = "utf-8"
        self.__init_colors()
        cs.curs_set(0)
        cs.resize_term(TER_LINES, TER_COLS)
        stdscr.refresh()
        self._init_menu()
        init()

    @property
    def menu(self):
        return self._menu_gui

    def game(self):
        return self._game_gui

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
        self._level_win = self._game_win.subwin(15, 28, 1, 15)
        self._stats_win = self._game_win.subwin(5, 54, 16, 2)
        self._game_gui = GameWindow(self._game_win, self._level_win, self._stats_win, TER_LINES, TER_COLS, level)

    def new_game(self, level):
        self._init_game_map(level)
        return self._game_gui

    def getkey(self):
        return self.stdscr.getkey()


