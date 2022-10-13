import curses as cs
from textgui.tguistatics import *
from curses.textpad import rectangle


class Menu:
    default_color = YELLOW

    def __init__(self, win_menu, lines, cols):
        self._win_menu = win_menu
        self._lines = lines
        self._cols = cols
        self.print_menu()
        self._selected_el = 0

    def print_menu(self):
        self._win_menu.clear()
        self._print_box()
        self._print_title()
        self._print_elements(menu_elements)
        self.refresh()

    def _print_box(self):
        self._win_menu.attron(cs.color_pair(self.default_color))
        self._win_menu.border()
        self._win_menu.attroff(cs.color_pair(self.default_color))

    def _print_title(self):
        self._win_menu.attron(cs.color_pair(self.default_color))
        for i in range(len(title)):
            self._win_menu.move(i+1, 2)
            self._win_menu.addstr(title[i])
        self._win_menu.attroff(cs.color_pair(self.default_color))

    def _print_elements(self, elements):
        self._win_menu.attron(cs.color_pair(self.default_color))
        j = 0
        for i in range(len(elements)):
            self._win_menu.move(j + len(title) + 2, self.center_x(self._cols, elements[i]))
            self._win_menu.addstr(elements[i])
            j += 2
        self._win_menu.attroff(cs.color_pair(self.default_color))

    def sel_el_changed(self, new_sel, option):
        self._win_menu.move(self._y_sel_el(self._selected_el), self.center_x(TER_COLS, all_elements[option][self._selected_el])-2)
        self._win_menu.addstr(" ")
        self._win_menu.move(self._y_sel_el(new_sel), self.center_x(TER_COLS, all_elements[option][new_sel])-2)
        self._win_menu.addstr(RIGHT_ARROW, cs.color_pair(self.default_color))
        self._selected_el = new_sel

    @staticmethod
    def center_x(cols, word):
        return (cols - len(word)) // 2

    @staticmethod
    def _y_sel_el(sel_el):
        return 11+(2*sel_el)

    def refresh(self):
        self._win_menu.refresh()
