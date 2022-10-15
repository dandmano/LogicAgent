import curses as cs
import logging

from textgui.tguistatics import *
from curses.textpad import rectangle


class MenuWindow:

    def __init__(self, win_menu, lines, cols):
        self._win_menu = win_menu
        self._lines = lines
        self._cols = cols
        self.print_main_menu()
        self._selected_el = 0

    def print_main_menu(self):
        self._selected_el = 0
        self._win_menu.clear()
        self._print_statics()
        self._print_elements(menu_elements)
        self.refresh()

    def print_difficulty_menu(self):
        self._selected_el = 1
        self._win_menu.clear()
        self._print_statics()
        self._print_elements(difficulty_elements)
        self.refresh()

    def sel_el_changed_menu(self, new_sel):
        self._win_menu.move((16+self._selected_el), self.center_x(TER_COLS, menu_elements[self._selected_el])-2)
        self._win_menu.addstr(" ")
        self._win_menu.move((16+new_sel), self.center_x(TER_COLS, menu_elements[new_sel])-2)
        self._win_menu.addstr(RIGHT_ARROW, cs.color_pair(YELLOW))
        self._selected_el = new_sel

    def sel_el_changed_difficulty(self, new_sel):
        new_sel += 1
        self._win_menu.move((16+self._selected_el), self.center_x(TER_COLS, difficulty_elements[self._selected_el])-2)
        self._win_menu.addstr(" ")
        self._win_menu.move((16+new_sel), self.center_x(TER_COLS, difficulty_elements[new_sel])-2)
        self._win_menu.addstr(RIGHT_ARROW, cs.color_pair(YELLOW))
        self._selected_el = new_sel

    def current_difficulty_change(self, new_dif):
        new_dif += 1
        self._win_menu.move(16, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(16, self.center_x(TER_COLS, difficulty_elements[new_dif]+difficulty_elements[0]))
        self._win_menu.addstr(difficulty_elements[0]+difficulty_elements[new_dif], cs.color_pair(YELLOW))

    def _print_statics(self):
        self._print_box()
        self._print_title()

    def _print_box(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.border()
        self._win_menu.attroff(cs.color_pair(YELLOW))

    def _print_title(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        for i in range(len(title)):
            self._win_menu.move(i+1, 2)
            self._win_menu.addstr(title[i])
        self._win_menu.attroff(cs.color_pair(YELLOW))

    def _print_elements(self, elements):
        self._win_menu.attron(cs.color_pair(YELLOW))
        for i in range(len(elements)):
            self._win_menu.move(i + len(title) + 2, self.center_x(self._cols, elements[i]))
            self._win_menu.addstr(elements[i])
        self._win_menu.attroff(cs.color_pair(YELLOW))

    @staticmethod
    def center_x(cols, word):
        return (cols - len(word)) // 2

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
