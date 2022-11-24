import pygame.draw
from logic.audiologic import get_sound_on
from gui.assetslogic import *
from gui.guistatics import *
from random import seed
from random import random


#  Klasa intrfejsu tekstowego obsugujaca rysowanie w oknie menu
class Menu:

    def __init__(self, screen, font, s_width, s_height):
        self._screen = screen
        self._font = font
        self._s_width = s_width
        self._s_height = s_height
        self._selected_el = 0
        self._ticks = 0
        self._curr_skin = 0
        seed(1)

    #  Metoda wyswietlajaca menu glowne
    def print_main_menu(self):
        self._screen.fill(BLACK)
        self._curr_skin = -1
        self._selected_el = 0
        self._print_statics()
        self._print_elements(menu_elements, 446)

    #  Metoda wyswietlajaca menu wyboru poziomu trudnosci
    def print_difficulty_menu(self):
        self._screen.fill(BLACK)
        self._curr_skin = -1
        self._selected_el = 0
        self._print_statics()
        self._print_elements(difficulty_elements, 488)

    #  Metoda wyswietlajaca menu wyboru skina
    def print_skin_menu(self):
        self._screen.fill(BLACK)
        self._selected_el = 1
        self._print_statics()
        self._print_skins()
        self._curr_skin = 0

    #  Metoda wyswietlajaca menu wyboru levela
    def print_level_menu(self):
        self._screen.fill(BLACK)
        self._selected_el = 0
        self._curr_skin = -1
        self._print_statics()
        self._print_levels()

    #  Metoda obsugujaca zmiane zaznaczonego elementu w menu glownym
    def sel_el_changed_menu(self, new_sel):
        img = self._font.render(ARROW, True, YELLOW)
        rect = img.get_rect()
        rect.center = (WIDTH_CENTER-(menu_elements_width[self._selected_el]/2)-20, 446 + self._selected_el*42)
        self._screen.fill(BLACK, rect)
        pygame.display.update(rect)
        rect.center = (WIDTH_CENTER-(menu_elements_width[new_sel]/2)-20, 446 + new_sel*42)
        self._screen.blit(img, rect)
        pygame.display.update(rect)
        self._selected_el = new_sel
        self._print_sound_helper()

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze poziomu trudnosci
    def sel_el_changed_difficulty(self, new_sel):
        img = self._font.render(ARROW, True, YELLOW)
        rect = img.get_rect()
        rect.center = (WIDTH_CENTER - (difficulty_elements_width[self._selected_el] / 2) - 20, 488 + self._selected_el * 42)
        self._screen.fill(BLACK, rect)
        pygame.display.update(rect)
        rect.center = (WIDTH_CENTER - (difficulty_elements_width[new_sel] / 2) - 20, 488 + new_sel * 42)
        self._screen.blit(img, rect)
        pygame.display.update(rect)
        self._selected_el = new_sel

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze skina
    def sel_skin_changed_skin(self, p, c, n):  # previous, current, next
        p, c, n = p % 4, c % 4, n % 4
        self._curr_skin = c
        sp, sc, sn = None, None, None
        if self._ticks % 30 == 0:
            sp = get_image(f"assets\\player\\{p}skin1.png")
            sc = get_image(f"assets\\player\\{c}skin2.png")
            sn = get_image(f"assets\\player\\{n}skin1.png")
        elif self._ticks % 15 == 0:
            sp = get_image(f"assets\\player\\{p}skin2.png")
            sc = get_image(f"assets\\player\\{c}skin1.png")
            sn = get_image(f"assets\\player\\{n}skin2.png")
        if sp is None:
            return
        sp = pygame.transform.scale(sp, (50, 50))
        sc = pygame.transform.scale(sc, (100, 100))
        sn = pygame.transform.scale(sn, (50, 50))
        self._screen.fill(BLACK, (self._s_width/2 - 51 - 70, 485, 50, 50))
        self._screen.fill(BLACK, (self._s_width/2 - 51, 461, 100, 100))
        self._screen.fill(BLACK, (self._s_width/2 + 47 + 16, 485, 50, 50))
        self._screen.blit(sp, (self._s_width/2 - 51 - 70, 485))
        self._screen.blit(sc, (self._s_width/2 - 51, 461))
        self._screen.blit(sn, (self._s_width/2 + 47 + 16, 485))
        pygame.display.update((260, 444, 280, 134))

    #  Metoda obsugujaca zmiane zaznaczonego elementu w wyborze levela
    def sel_level_changed(self, levels, p, c, n):
        j = 488
        tmp = [p, c, n]
        for i in range(len(tmp)):
            color = YELLOW_DIM
            if i == 1:
                color = YELLOW
            img = self._font.render(levels[tmp[i]].name, True, color, BLACK)
            rect = img.get_rect()
            rect.center = (WIDTH_CENTER, j)
            self._screen.fill(BLACK, (rect.x-15, rect.y, rect.width + 30, rect.height))
            self._screen.blit(img, rect)
            pygame.display.update((rect.x-15, rect.y, rect.width + 30, rect.height))
            j += 42

    #  Metoda obsugujaca zmiane wybranego poziomu trudnosci
    def current_difficulty_change(self, dif):
        text = f"CURRENT = {difficulty_elements[dif]}"
        img = self._font.render(text, True, YELLOW, BLACK)
        rect = img.get_rect()
        rect.center = (WIDTH_CENTER, 446)
        self._screen.blit(img, rect)
        pygame.display.update(rect)

    def tick(self):
        if self._ticks > 100000:
            self._ticks = 0
        self._ticks += 1
        self._print_title()
        if self._curr_skin >= 0:
            self.sel_skin_changed_skin(self._curr_skin-1, self._curr_skin, self._curr_skin+1)

    #  Metoda wypisujaca elmenty statyczne okna takie jak tytyul oraz obramowanie
    def _print_statics(self):
        self._ticks = 0
        self._print_box()
        self._print_title()
        pygame.display.update()

    #  Metoda rysujaca obramowanie wokol okna
    def _print_box(self):
        pygame.draw.rect(self._screen, YELLOW, (0, 0, self._s_width, self._s_height), 2)
        pygame.draw.rect(self._screen, YELLOW, (6, 6, self._s_width-12, self._s_height-12), 2)

    #  Metoda rysujaca tytul gry
    def _print_title(self):
        title_image = None
        if self._ticks % 60 == 0:
            title_image = get_image("assets\\logicagent-half.png")
        elif self._ticks % 30 == 0:
            title_image = get_image("assets\\logicagent-trans.png")
        if title_image is None:
            return
        title_image = pygame.transform.scale(title_image, TITLE_SIZE)
        rect = title_image.get_rect()
        rect.center = (self._s_width/2, rect.height/2+30)
        self._screen.fill(BLACK, rect)
        self._screen.blit(title_image, rect)
        pygame.display.update(rect)

    #  Metoda wypisujaca elementy menu glownego lub poziomu trudnosci
    def _print_elements(self, elements, j):
        # j = 446 or 448
        for i in range(len(elements)):
            img = self._font.render(elements[i], True, YELLOW, BLACK)
            rect = img.get_rect()
            rect.center = (WIDTH_CENTER, j)
            self._screen.blit(img, rect)
            pygame.display.update(rect)
            j += 42

    #  Metoda rysujaca menu wyboru skina
    def _print_skins(self):
        pygame.draw.rect(self._screen, YELLOW, (260, 444, 280, 134), 3)
        pygame.draw.rect(self._screen, YELLOW, (self._s_width/2 - 54, 458, 106, 106), 3)
        pygame.draw.rect(self._screen, YELLOW_DIM, (self._s_width/2 - 54 - 70, 482, 56, 56), 3)
        pygame.draw.rect(self._screen, YELLOW_DIM, (self._s_width/2 + 50 + 16, 482, 56, 56), 3)
        pygame.display.update((260, 444, 280, 134))

    #  Metoda rysujaca elementy menu wyboru levela
    def _print_levels(self):
        text = "CHOOSE LEVEL:"
        img = self._font.render(text, True, YELLOW, BLACK)
        rect = img.get_rect()
        rect.center = (WIDTH_CENTER, 446)
        self._screen.blit(img, rect)
        pygame.display.update(rect)

    #  Metoda rysujaca tekst informujacy o stanie dzwieku (wlaczony/wylaczony)
    def _print_sound_helper(self):
        if get_sound_on():
            img = get_image("assets\\unmute.png")
        else:
            img = get_image("assets\\mute.png")
        rect = img.get_rect()
        rect.x, rect.y = 16, 552
        self._screen.fill(BLACK, rect)
        self._screen.blit(img, rect)
        pygame.display.update(rect)

    def refresh(self):
        pass


# Klasa interfesju tekstowego obslugujaca wyswietlanie i rysowanie obrazu gry, statystyk oraz endgame screena
class Game:
    win_x = 73
    win_y = 55
    win_width = 25*26
    win_heigth = 25*13
    stats_x = 73
    stats_y = 437
    stats_width = win_width
    stats_height = 117
    cell_x = 25
    cell_y = 25
    level_cells_y = 14  # 13* ale od 1
    level_cells_x = 27  # 26* ale od 1

    def __init__(self, screen, font, s_width, s_height, level):
        self._screen = screen
        self._font = font
        self._s_width = s_width
        self._s_height = s_height
        self._level = level
        self._draw()

    #  Metoda rysujaca rysujaca gracza na nowej pozycji i przywracajaca stary element mapy na poprzedniej pozycji gracza
    def draw_player(self, skin, tmpx, tmpy, x, y, mapelement=0, bluepu=False, orangepu=False, magentapu=False):
        pass
        # self._level_win.move(tmpy + 1, tmpx + 1)
        # match mapelement:
        #     case 0:
        #         self._level_win.addstr(BLANK)
        #     case 5:
        #         if bluepu:
        #             self._level_win.addstr(WALL, cs.color_pair(BLUE_DIM))
        #         else:
        #             self._level_win.addstr(WALL, cs.color_pair(BLUE))
        #     case 7:
        #         if orangepu:
        #             self._level_win.addstr(WALL, cs.color_pair(ORANGE_DIM))
        #         else:
        #             self._level_win.addstr(WALL, cs.color_pair(ORANGE))
        #     case 9:
        #         if magentapu:
        #             self._level_win.addstr(WALL, cs.color_pair(MAGENTA_DIM))
        #         else:
        #             self._level_win.addstr(WALL, cs.color_pair(MAGENTA))
        #     case _:
        #         raise Exception("draw player map element exception")
        # self._level_win.move(y + 1, x + 1)
        # self._level_win.addstr(skins[skin], cs.color_pair(YELLOW))
        # self.refresh()

    #  Metoda przerysowujaca statystki gry (czas, power-upy)
    def update_stats(self, game_time, bluepu, orangepu, magentapu, level_name):
        pass
        # self._stats_win.attron(cs.color_pair(YELLOW))
        #
        # self._stats_win.move(2, 2)
        # self._stats_win.addstr(level_name)
        #
        # self._stats_win.move(2, 18)
        # self._stats_win.addstr("Power ups: ")
        #
        # self._stats_win.move(2, 29)
        # if bluepu:
        #     self._stats_win.addstr(STAR, cs.color_pair(BLUE))
        # else:
        #     self._stats_win.addstr(STAR, cs.color_pair(BLUE_DIM))
        # self._stats_win.move(2, 31)
        # if orangepu:
        #     self._stats_win.addstr(STAR, cs.color_pair(ORANGE))
        # else:
        #     self._stats_win.addstr(STAR, cs.color_pair(ORANGE_DIM))
        # self._stats_win.move(2, 33)
        # if magentapu:
        #     self._stats_win.addstr(STAR, cs.color_pair(MAGENTA))
        # else:
        #     self._stats_win.addstr(STAR, cs.color_pair(MAGENTA_DIM))
        #
        # self._stats_win.move(2, 42)
        # self._stats_win.addstr("Time: ")
        #
        # self._stats_win.move(2, 48)
        # self._stats_win.addstr("   ")
        # self._stats_win.move(2, 48)
        # self._stats_win.addstr(str(game_time))
        #
        # self._stats_win.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca okno gry
    def _draw(self):
        self._screen.fill(BLACK)
        self._draw_title()
        self._draw_level()
        self._draw_borders()

    #  Metoda rysujaca przyciemniony tytul
    def _draw_title(self):
        title_image = get_image("assets\\logicagent-trans-dim.png")
        title_image = pygame.transform.scale(title_image, TITLE_SIZE)
        rect = title_image.get_rect()
        rect.center = (self._s_width / 2, rect.height / 2 + 30)
        self._screen.fill(BLACK, rect)
        self._screen.blit(title_image, rect)
        pygame.display.update(rect)

    #  Metoda wybierjaca wariant ekranu koncowego
    def endgame(self, end_type):
        pass
        # self._game_win.clear()
        # if type == 1:
        #     self._draw_endgame_lost()
        # else:
        #     self._draw_endgame_win()
        # self.refresh()

    #  Metoda rysujaca ekran koncowy - przegrana
    def _draw_endgame_lost(self):
        pass
        # text1 = "YOU LOST"
        # text2 = "(PRESS SPACE TO CONTINUE)"
        # self._game_win.attron(cs.color_pair(RED))
        # for i in range(len(dead_screen)):
        #     self._game_win.move(i + 1, 2)
        #     self._game_win.addstr(dead_screen[i])
        # self._game_win.move(len(dead_screen) + 2, (self._cols - len(text1)) // 2)
        # self._game_win.addstr(text1)
        # self._game_win.move(len(dead_screen) + 4, (self._cols - len(text2)) // 2)
        # self._game_win.addstr(text2)
        # self._game_win.attroff(cs.color_pair(RED))

    #  Metoda rysujaca ekran koncowy - zwyciestwo
    def _draw_endgame_win(self):
        pass
        # text1 = "YOU WON! :)"
        # text2 = "(PRESS SPACE TO CONTINUE)"
        # self._game_win.attron(cs.color_pair(YELLOW))
        # for i in range(len(title)):
        #     self._game_win.move(i + 1, 2)
        #     self._game_win.addstr(title[i])
        # self._game_win.move(len(title) + 2, (self._cols - len(text1)) // 2)
        # self._game_win.addstr(text1)
        # self._game_win.move(len(title) + 4, (self._cols - len(text2)) // 2)
        # self._game_win.addstr(text2)
        # self._game_win.attroff(cs.color_pair(YELLOW))

    #  Metoda rysujaca obramowania - obramowanie gry, obramowanie statystyk i obramowanie okna
    def _draw_borders(self):
        pygame.draw.rect(self._screen, YELLOW, (0, 0, self._s_width, self._s_height), 2)
        pygame.draw.rect(self._screen, YELLOW, (6, 6, self._s_width - 12, self._s_height - 12), 2)
        pygame.draw.rect(self._screen, YELLOW, (self.win_x-3, self.win_y-3, self.win_width+6, self.win_heigth+6), 3)
        self._screen.fill(BLACK, (self.win_x, self.win_y, self.win_width, self.win_heigth))
        pygame.draw.rect(self._screen, YELLOW, (self.stats_x-3, self.stats_y-3, self.win_width+6, self.stats_height+6), 3)
        self._screen.fill(BLACK, (self.stats_x, self.stats_y, self.stats_width, self.stats_height))
        pygame.display.update()

    #  Metoda rysujaca level gry (mape)
    def _draw_level(self):
        pass
        # for y in range(13):
        #     for x in range(26):
        #         self._level_win.move(y + 1, x + 1)
        #         # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
        #         # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
        #         match self._level[y][x]:
        #             case 0:
        #                 self._level_win.addstr(" ")
        #             case 1:
        #                 self._level_win.addstr(WALL, cs.color_pair(WHITE))
        #             case 2:
        #                 self._level_win.addstr(WALL, cs.color_pair(GREEN))
        #             case 3:
        #                 self._level_win.addstr(SPIKES, cs.color_pair(RED))
        #             case 4:
        #                 self._level_win.addstr(STAR, cs.color_pair(BLUE))
        #             case 5:
        #                 self._level_win.addstr(WALL, cs.color_pair(BLUE))
        #             case 6:
        #                 self._level_win.addstr(STAR, cs.color_pair(ORANGE))
        #             case 7:
        #                 self._level_win.addstr(WALL, cs.color_pair(ORANGE))
        #             case 8:
        #                 self._level_win.addstr(STAR, cs.color_pair(MAGENTA))
        #             case 9:
        #                 self._level_win.addstr(WALL, cs.color_pair(MAGENTA))

    #  Metoda przerysowujaca elementy mapy zmieniajace sie w trakcie gry (kolorowe sciany, power-upy)
    def redraw_level(self, bluepu, orangepu, magentapu):
        pass
        # for y in range(13):
        #     for x in range(26):
        #         self._level_win.move(y + 1, x + 1)
        #         # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
        #         # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
        #         match self._level[y][x]:
        #             case 5:
        #                 if bluepu:
        #                     self._level_win.addstr(WALL, cs.color_pair(BLUE_DIM))
        #             case 7:
        #                 if orangepu:
        #                     self._level_win.addstr(WALL, cs.color_pair(ORANGE_DIM))
        #             case 9:
        #                 if magentapu:
        #                     self._level_win.addstr(WALL, cs.color_pair(MAGENTA_DIM))


    def refresh(self):
        pass
