import curses as cs
import logging

from textgui.tguistatics import *
from curses.textpad import rectangle


class MenuWindow:
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


class GameWindow:
    default_color = YELLOW
    level_y = 13
    level_x = 21

    def __init__(self, win_game, level_win, lines, cols, level):
        self._win_game = win_game
        self._level_win = level_win
        self._lines = lines
        self._cols = cols
        self._level = level
        self._draw()

    def _draw(self):
        self._print_boxes()
        self.refresh_game()
        self._draw_level()
        self.refresh_level()

    def _print_boxes(self):
        self._win_game.attron(cs.color_pair(self.default_color))
        self._win_game.border()
        rectangle(self._win_game, 1, 16, 14, 37)
        self._win_game.attroff(cs.color_pair(self.default_color))

    def _draw_level(self):
        for y in range(12):
            for x in range(20):
                self._level_win.move(y, x)
                match self._level[y][x]:
                    case 0:
                        self._level_win.addstr(" ")
                    case 1:
                        self._level_win.addstr(WALL, cs.color_pair(WHITE))
                    case 2:
                        self._level_win.addstr(WALL, cs.color_pair(GREEN))

    def draw_player(self, tmpx, tmpy, x, y, pos):  # 0 - up 1 - down 2 - left 3 - right
        self._level_win.move(tmpy, tmpx)
        self._level_win.addstr(BLANK)
        self._level_win.move(y, x)
        match pos:
            case 0:
                self._level_win.addstr(P_UP, cs.color_pair(self.default_color))
            case 1:
                self._level_win.addstr(P_DOWN, cs.color_pair(self.default_color))
            case 2:
                self._level_win.addstr(P_LEFT, cs.color_pair(self.default_color))
            case 3:
                self._level_win.addstr(P_RIGHT, cs.color_pair(self.default_color))
        self.refresh_level()

    def refresh_game(self):
        self._win_game.refresh()
    def refresh_level(self):
        self._level_win.refresh()
