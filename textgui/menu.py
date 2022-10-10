import curses as cs
from textgui.tguistatics import *


class Menu:
    elements = ["PLAY", "CREATE LEVEL", "SETTINGS", "EXIT"]
    title = [
        r"  __________  _______    _   __________    ______",
        r" /_  __/ __ \/  _/   |  / | / / ____/ /   / ____/",
        r"  / / / /_/ // // /| | /  |/ / / __/ /   / __/   ",
        r" / / / _, _// // ___ |/ /|  / /_/ / /___/ /___   ",
        r"/_/ /_/ |_/___/_/  |_/_/_|_/\____/_____/_____/   ",
        r"            /   | / ____/ ____/ | / /_  __/      ",
        r"           / /| |/ / __/ __/ /  |/ / / /         ",
        r"          / ___ / /_/ / /___/ /|  / / /          ",
        r"         /_/  |_\____/_____/_/ |_/ /_/           "]

    def __init__(self, win_menu, lines, cols):
        self._win_menu = win_menu
        self._lines = lines
        self._cols = cols
        self._print_title()
        self._print_box()
        self._print_elements()
        self._selected_el = 0

    def _print_box(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.border()
        self._win_menu.attroff(cs.color_pair(YELLOW))

    def _print_title(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        for i in range(len(self.title)):
            self._win_menu.move(i+1, 2)
            self._win_menu.addstr(self.title[i])
        self._win_menu.attroff(cs.color_pair(YELLOW))

    def _print_elements(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        j = 0
        for i in range(len(self.elements)):
            self._win_menu.move(j + len(self.title) + 2, center_x(self._cols, self.elements[i]))
            self._win_menu.addstr(self.elements[i])
            j += 2
        self._win_menu.attroff(cs.color_pair(YELLOW))

    def sel_el_changed(self):
        pass

    def draw_menu(self):
        self._win_menu.refresh()
