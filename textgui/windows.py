import curses as cs

from textgui.tguistatics import *


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
    level_y = 14
    level_x = 27

    def __init__(self, game_win, level_win, stats_win, lines, cols, level):
        self._game_win = game_win
        self._level_win = level_win
        self._stats_win = stats_win
        self._lines = lines
        self._cols = cols
        self._level = level
        self._draw()

    def draw_player(self, tmpx, tmpy, x, y, mapelement=0):
        self._level_win.move(tmpy+1, tmpx+1)
        match mapelement:
            case 0:
                self._level_win.addstr(BLANK)
            case 5:
                self._level_win.addstr(WALL, cs.color_pair(BLUE))
            case 7:
                self._level_win.addstr(WALL, cs.color_pair(ORANGE))
            case 9:
                self._level_win.addstr(WALL, cs.color_pair(MAGENTA))
            case _:
                raise Exception("draw player map element exception")
        self._level_win.move(y+1, x+1)
        self._level_win.addstr(PLAYER, cs.color_pair(YELLOW))
        self.refresh()

    def update_stats(self, game_time, bluepu, orangepu, magentapu, lives):
        self._stats_win.attron(cs.color_pair(YELLOW))

        self._stats_win.move(2, 2)
        self._stats_win.addstr("Lives: ")

        self._stats_win.move(2, 10)
        self._stats_win.addstr(str(lives))

        self._stats_win.move(2, 18)
        self._stats_win.addstr("Power ups: ")

        self._stats_win.move(2, 2)
        self._stats_win.addstr("Time: ")

        self._stats_win.attroff(cs.color_pair(YELLOW))


    def _draw(self):
        self._draw_title()
        self._draw_level()
        self._draw_borders()
        self.refresh()

    def _draw_title(self):
        self._game_win.attron(cs.color_pair(YELLOW_DIM))
        for i in range(len(title)):
            self._game_win.move(i+1, 2)
            self._game_win.addstr(title[i])
        self._game_win.attroff(cs.color_pair(YELLOW_DIM))

    def _draw_borders(self):
        self._game_win.attron(cs.color_pair(YELLOW))
        self._level_win.attron(cs.color_pair(YELLOW))
        self._stats_win.attron(cs.color_pair(YELLOW))
        self._game_win.border()
        self._level_win.border()
        self._stats_win.border()
        self._game_win.attroff(cs.color_pair(YELLOW))
        self._level_win.attroff(cs.color_pair(YELLOW))
        self._stats_win.attroff(cs.color_pair(YELLOW))

    def _draw_level(self):
        for y in range(13):
            for x in range(26):
                self._level_win.move(y+1, x+1)
                # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
                # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
                match self._level[y][x]:
                    case 0:
                        self._level_win.addstr(" ")
                    case 1:
                        self._level_win.addstr(WALL, cs.color_pair(WHITE))
                    case 2:
                        self._level_win.addstr(WALL, cs.color_pair(GREEN))
                    case 3:
                        self._level_win.addstr(SPIKES, cs.color_pair(RED))
                    case 4:
                        self._level_win.addstr(STAR, cs.color_pair(BLUE))
                    case 5:
                        self._level_win.addstr(WALL, cs.color_pair(BLUE))
                    case 6:
                        self._level_win.addstr(STAR, cs.color_pair(ORANGE))
                    case 7:
                        self._level_win.addstr(WALL, cs.color_pair(ORANGE))
                    case 8:
                        self._level_win.addstr(STAR, cs.color_pair(MAGENTA))
                    case 9:
                        self._level_win.addstr(WALL, cs.color_pair(MAGENTA))
                    case 99:
                        self.draw_player(x, y, x, y)

    def refresh(self):
        self._game_win.touchwin()
        self._game_win.refresh()
        self._level_win.refresh()
        self._stats_win.refresh()

