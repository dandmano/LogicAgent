import curses as cs
from textgui.menu import Menu
from textgui.tguistatics import *


class TGui:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        # self.stdscr.nodelay(True)
        self.stdscr.encoding = "utf-8"
        self.__init_colors()
        cs.curs_set(0)
        cs.resize_term(TER_LINES, TER_COLS)
        stdscr.refresh()
        self._init_menu()

    @property
    def menu(self):
        return self._menu

    @staticmethod
    def __init_colors():
        cs.start_color()
        cs.use_default_colors()
        for i in range(0, 255):
            cs.init_pair(i + 1, i, -1)

    def _init_menu(self):
        self._menu_win = cs.newwin(TER_LINES, TER_COLS, 0, 0)
        self._menu = Menu(self._menu_win, TER_LINES, TER_COLS)

    def getkey(self):
        return self.stdscr.getkey()


