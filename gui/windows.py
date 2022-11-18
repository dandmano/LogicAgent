import curses as cs
from curses.textpad import rectangle
from logic.audiologic import get_sound_on

from textgui.tguistatics import *

#  Klasa intrfejsu tekstowego obsugujaca rysowanie w oknie menu
class MenuWindow:

    def __init__(self, win_menu, lines, cols):
        self._win_menu = win_menu
        self._lines = lines
        self._cols = cols
        self.print_main_menu()
        self._selected_el = 0

    #  Metoda wyswietlajaca menu glowne
    def print_main_menu(self):
        self._selected_el = 0
        self._win_menu.clear()
        self._print_statics()
        self._print_elements(menu_elements)
        self.refresh()

    #  Metoda wyswietlajaca menu wyboru poziomu trudnosci
    def print_difficulty_menu(self):
        self._selected_el = 1
        self._win_menu.clear()
        self._print_statics()
        self._print_elements(difficulty_elements)
        self.refresh()

    #  Metoda wyswietlajaca menu wyboru skina
    def print_skin_menu(self):
        self._selected_el = 1
        self._win_menu.clear()
        self._print_statics()
        self._print_skins()
        self.refresh()

    #  Metoda wyswietlajaca menu wyboru levela
    def print_level_menu(self):
        self._win_menu.clear()
        self._print_statics()
        self._print_levels()
        self.refresh()

    #  Metoda obsugujaca zmiane zaznaczonego elementu w menu glownym
    def sel_el_changed_menu(self, new_sel):
        self._win_menu.move((16 + self._selected_el), self.center_x(TER_COLS, menu_elements[self._selected_el]) - 2)
        self._win_menu.addstr(" ")
        self._win_menu.move((16 + new_sel), self.center_x(TER_COLS, menu_elements[new_sel]) - 2)
        self._win_menu.addstr(RIGHT_ARROW, cs.color_pair(YELLOW))
        self._selected_el = new_sel
        self._print_sound_helper()

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze poziomu trudnosci
    def sel_el_changed_difficulty(self, new_sel):
        new_sel += 1
        self._win_menu.move((16 + self._selected_el),
                            self.center_x(TER_COLS, difficulty_elements[self._selected_el]) - 2)
        self._win_menu.addstr(" ")
        self._win_menu.move((16 + new_sel), self.center_x(TER_COLS, difficulty_elements[new_sel]) - 2)
        self._win_menu.addstr(RIGHT_ARROW, cs.color_pair(YELLOW))
        self._selected_el = new_sel

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze skina
    def sel_skin_changed_skin(self, p, c, n):  # previous, current, next
        recy = len(title) + 3
        recx = 22
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.move(recy + 1, recx + 1)
        self._win_menu.addstr(f" {skins[p]} {RIGHT_ARROW} {skins[c]} {LEFT_ARROW} {skins[n]}")
        self._win_menu.attroff(cs.color_pair(YELLOW))
        self.refresh()

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze levela
    def sel_level_changed(self, levels, p, c, n):
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.move(len(title) + 3, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(len(title) + 3, self.center_x(self._cols, levels[p].name))
        self._win_menu.addstr(levels[p].name, cs.color_pair(YELLOW_DIM))
        self._win_menu.move(len(title) + 4, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(len(title) + 4, self.center_x(self._cols, levels[c].name))
        self._win_menu.addstr(levels[c].name)
        self._win_menu.move(len(title) + 5, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(len(title) + 5, self.center_x(self._cols, levels[n].name))
        self._win_menu.addstr(levels[n].name, cs.color_pair(YELLOW_DIM))
        self._win_menu.attroff(cs.color_pair(YELLOW))
        self.refresh()

    #  Metoda obsugujaca zmiane wybranego poziomu trudnosci
    def current_difficulty_change(self, new_dif):
        new_dif += 1
        self._win_menu.move(16, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(16, self.center_x(TER_COLS, difficulty_elements[new_dif] + difficulty_elements[0]))
        self._win_menu.addstr(difficulty_elements[0] + difficulty_elements[new_dif], cs.color_pair(YELLOW))
        self.refresh()

    #  Metoda wypisujaca elmenty statyczne okna takie jak tytyul oraz obramowanie
    def _print_statics(self):
        self._print_box()
        self._print_title()

    #  Metoda rysujaca obramowanie wokol okna
    def _print_box(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.border()
        self._win_menu.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca tytul gry
    def _print_title(self):
        self._win_menu.attron(cs.color_pair(YELLOW))
        for i in range(len(title)):
            self._win_menu.move(i + 1, 2)
            self._win_menu.addstr(title[i])
        self._win_menu.attroff(cs.color_pair(YELLOW))

    #  Metoda wypisujaca elementy menu glownego lub poziomu trudnosci
    def _print_elements(self, elements):
        self._win_menu.attron(cs.color_pair(YELLOW))
        for i in range(len(elements)):
            self._win_menu.move(i + len(title) + 2, self.center_x(self._cols, elements[i]))
            self._win_menu.addstr(elements[i])
        self._win_menu.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca menu wyboru skina
    def _print_skins(self):
        text1 = "SKIN:"
        text2 = "(PRESS SPACE TO ACCEPT)"
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.move(len(title) + 2, self.center_x(self._cols, text1))
        self._win_menu.addstr(text1)
        rectangle(self._win_menu, len(title) + 3, 22, len(title) + 5, 34)
        self._win_menu.move(len(title) + 6, self.center_x(self._cols, text2))
        self._win_menu.addstr(text2)
        self._win_menu.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca elementy menu wyboru levela
    def _print_levels(self):
        text1 = "Choose level:"
        text2 = "(PRESS SPACE TO ACCEPT)"
        self._win_menu.attron(cs.color_pair(YELLOW))
        self._win_menu.move(len(title) + 2, self.center_x(self._cols, text1))
        self._win_menu.addstr(text1)
        self._win_menu.move(len(title) + 6, self.center_x(self._cols, text2))
        self._win_menu.addstr(text2)
        self._win_menu.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca tekst informujacy o stanie dzwieku (wlaczony/wylaczony)
    def _print_sound_helper(self):
        self._win_menu.move(self._lines - 2, 1)
        self._win_menu.addstr(empty_line)
        self._win_menu.move(self._lines - 2, 3)
        if get_sound_on():
            self._win_menu.addstr("PRESS 'M' TO MUTE", cs.color_pair(YELLOW))
        else:
            self._win_menu.addstr("PRESS 'M' TO UNMUTE", cs.color_pair(YELLOW_DIM))

    @staticmethod
    def center_x(cols, word):
        return (cols - len(word)) // 2

    def refresh(self):
        self._win_menu.refresh()


# Klasa interfesju tekstowego obslugujaca wyswietlanie i rysowanie obrazu gry, statystyk oraz endgame screena
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

    #  Metoda rysujaca rysujaca gracza na nowej pozycji i przywracajaca stary element mapy na poprzedniej pozycji gracza
    def draw_player(self, skin, tmpx, tmpy, x, y, mapelement=0, bluepu=False, orangepu=False, magentapu=False):
        self._level_win.move(tmpy + 1, tmpx + 1)
        match mapelement:
            case 0:
                self._level_win.addstr(BLANK)
            case 5:
                if bluepu:
                    self._level_win.addstr(WALL, cs.color_pair(BLUE_DIM))
                else:
                    self._level_win.addstr(WALL, cs.color_pair(BLUE))
            case 7:
                if orangepu:
                    self._level_win.addstr(WALL, cs.color_pair(ORANGE_DIM))
                else:
                    self._level_win.addstr(WALL, cs.color_pair(ORANGE))
            case 9:
                if magentapu:
                    self._level_win.addstr(WALL, cs.color_pair(MAGENTA_DIM))
                else:
                    self._level_win.addstr(WALL, cs.color_pair(MAGENTA))
            case _:
                raise Exception("draw player map element exception")
        self._level_win.move(y + 1, x + 1)
        self._level_win.addstr(skins[skin], cs.color_pair(YELLOW))
        self.refresh()

    #  Metoda przerysowujaca statystki gry (czas, power-upy)
    def update_stats(self, game_time, bluepu, orangepu, magentapu, level_name):
        self._stats_win.attron(cs.color_pair(YELLOW))

        self._stats_win.move(2, 2)
        self._stats_win.addstr(level_name)

        self._stats_win.move(2, 18)
        self._stats_win.addstr("Power ups: ")

        self._stats_win.move(2, 29)
        if bluepu:
            self._stats_win.addstr(STAR, cs.color_pair(BLUE))
        else:
            self._stats_win.addstr(STAR, cs.color_pair(BLUE_DIM))
        self._stats_win.move(2, 31)
        if orangepu:
            self._stats_win.addstr(STAR, cs.color_pair(ORANGE))
        else:
            self._stats_win.addstr(STAR, cs.color_pair(ORANGE_DIM))
        self._stats_win.move(2, 33)
        if magentapu:
            self._stats_win.addstr(STAR, cs.color_pair(MAGENTA))
        else:
            self._stats_win.addstr(STAR, cs.color_pair(MAGENTA_DIM))

        self._stats_win.move(2, 42)
        self._stats_win.addstr("Time: ")

        self._stats_win.move(2, 48)
        self._stats_win.addstr("   ")
        self._stats_win.move(2, 48)
        self._stats_win.addstr(str(game_time))

        self._stats_win.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca okno gry
    def _draw(self):
        self._draw_title()
        self._draw_level()
        self._draw_borders()
        self.refresh()

    #  Metoda rysujaca przyciemniony tytul
    def _draw_title(self):
        self._game_win.attron(cs.color_pair(YELLOW_DIM))
        for i in range(len(title)):
            self._game_win.move(i + 1, 2)
            self._game_win.addstr(title[i])
        self._game_win.attroff(cs.color_pair(YELLOW_DIM))

    #  Metoda wybierjaca wariant ekranu koncowego
    def endgame(self, type):
        self._game_win.clear()
        if type == 1:
            self._draw_endgame_lost()
        else:
            self._draw_endgame_win()
        self.refresh()

    #  Metoda rysujaca ekran koncowy - przegrana
    def _draw_endgame_lost(self):
        text1 = "YOU LOST"
        text2 = "(PRESS SPACE TO CONTINUE)"
        self._game_win.attron(cs.color_pair(RED))
        for i in range(len(dead_screen)):
            self._game_win.move(i + 1, 2)
            self._game_win.addstr(dead_screen[i])
        self._game_win.move(len(dead_screen) + 2, (self._cols - len(text1)) // 2)
        self._game_win.addstr(text1)
        self._game_win.move(len(dead_screen) + 4, (self._cols - len(text2)) // 2)
        self._game_win.addstr(text2)
        self._game_win.attroff(cs.color_pair(RED))

    #  Metoda rysujaca ekran koncowy - zwyciestwo
    def _draw_endgame_win(self):
        text1 = "YOU WON! :)"
        text2 = "(PRESS SPACE TO CONTINUE)"
        self._game_win.attron(cs.color_pair(YELLOW))
        for i in range(len(title)):
            self._game_win.move(i + 1, 2)
            self._game_win.addstr(title[i])
        self._game_win.move(len(title) + 2, (self._cols - len(text1)) // 2)
        self._game_win.addstr(text1)
        self._game_win.move(len(title) + 4, (self._cols - len(text2)) // 2)
        self._game_win.addstr(text2)
        self._game_win.attroff(cs.color_pair(YELLOW))


    #  Metoda rysujaca obramowania - obramowanie gry, obramowanie statystyk i obramowanie okna
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

    #  Metoda rysujaca level gry (mape)
    def _draw_level(self):
        for y in range(13):
            for x in range(26):
                self._level_win.move(y + 1, x + 1)
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

    #  Metoda przerysowujaca elementy mapy zmieniajace sie w trakcie gry (kolorowe sciany, power-upy)
    def redraw_level(self, bluepu, orangepu, magentapu):
        for y in range(13):
            for x in range(26):
                self._level_win.move(y + 1, x + 1)
                # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
                # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
                match self._level[y][x]:
                    case 5:
                        if bluepu:
                            self._level_win.addstr(WALL, cs.color_pair(BLUE_DIM))
                    case 7:
                        if orangepu:
                            self._level_win.addstr(WALL, cs.color_pair(ORANGE_DIM))
                    case 9:
                        if magentapu:
                            self._level_win.addstr(WALL, cs.color_pair(MAGENTA_DIM))


    def refresh(self):
        self._game_win.touchwin()
        self._game_win.refresh()
        self._level_win.refresh()
        self._stats_win.refresh()
