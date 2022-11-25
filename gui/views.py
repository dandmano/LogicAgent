import pygame.draw
from logic.audiologic import get_sound_on
from gui.assetslogic import *
from gui.guistatics import *
from random import seed
from random import random


#  Klasa intrfejsu tekstowego obsugujaca rysowanie w oknie menu
class Menu:
    _selected_el = 0
    _ticks = 0
    _curr_skin = 0
    _main_menu_rects = []
    _difficulty_menu_rects = []
    _skins_menu_rects = []
    _levels_menu_rects = []
    _mute_rect = 0

    def __init__(self, screen, font, s_width, s_height):
        self._screen = screen
        self._font = font
        self._s_width = s_width
        self._s_height = s_height
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
        sp, sc, sn = None, None, None
        if self._curr_skin != c:
            self._ticks = 0
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
        self._curr_skin = c
        sp = pygame.transform.scale(sp, (50, 50))
        sc = pygame.transform.scale(sc, (100, 100))
        sn = pygame.transform.scale(sn, (50, 50))
        self._screen.fill(BLACK, (self._s_width/2 - 51 - 70, 485, 50, 50))
        self._screen.fill(BLACK, (self._s_width/2 - 51, 461, 100, 100))
        self._screen.fill(BLACK, (self._s_width/2 + 47 + 22, 485, 50, 50))
        self._screen.blit(sp, (self._s_width/2 - 51 - 70, 485))
        self._screen.blit(sc, (self._s_width/2 - 51, 461))
        self._screen.blit(sn, (self._s_width/2 + 47 + 22, 485))
        pygame.display.update((260, 444, 280, 134))
        if len(self._skins_menu_rects) < 3:
            self._skins_menu_rects.append(pygame.Rect(self._s_width/2 - 51 - 70, 485, 50, 50))
            self._skins_menu_rects.append(pygame.Rect(self._s_width/2 - 51, 461, 100, 100))
            self._skins_menu_rects.append(pygame.Rect(self._s_width/2 + 47 + 22, 485, 50, 50))

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
            if len(self._levels_menu_rects) < 3:
                self._levels_menu_rects.append(rect)

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
        # j = 446 or 488
        for i in range(len(elements)):
            img = self._font.render(elements[i], True, YELLOW, BLACK)
            rect = img.get_rect()
            rect.center = (WIDTH_CENTER, j)
            self._screen.blit(img, rect)
            pygame.display.update(rect)
            j += 42
            if len(elements) == 4 and len(self._main_menu_rects)<4:
                self._main_menu_rects.append(rect)
            elif len(self._difficulty_menu_rects)<3:
                self._difficulty_menu_rects.append(rect)

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
        if self._mute_rect == 0:
            self._mute_rect = rect

    def main_menu_mouse_press(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self._main_menu_rects)):
            if self._main_menu_rects[i].collidepoint(mouse_pos):
                return i
        if self._mute_rect.collidepoint(mouse_pos):
            return -10
        return -1

    def difficulty_menu_mouse_press(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self._difficulty_menu_rects)):
            if self._difficulty_menu_rects[i].collidepoint(mouse_pos):
                return i
        return -1

    def skins_menu_mouse_press(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self._skins_menu_rects)):
            if self._skins_menu_rects[i].collidepoint(mouse_pos):
                return i-1
        return -5

    def level_menu_mouse_press(self):
        mouse_pos = pygame.mouse.get_pos()
        for i in range(len(self._levels_menu_rects)):
            if self._levels_menu_rects[i].collidepoint(mouse_pos):
                return i - 1
        return -5
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
        self._moving_dir = 1  # 1 down, -1 up, 2 right, -2 left
        self._player_x = 0
        self._player_y = 0
        self._ticks = 0
        self._skin = -1
        self._draw()

    #  Metoda rysujaca rysujaca gracza na nowej pozycji i przywracajaca stary element mapy na poprzedniej pozycji gracza
    def draw_player(self, skin, tmpx, tmpy, x, y, mapelement=0, bluepu=False, orangepu=False, magentapu=False):
        old_tile = (self.win_x+tmpx*25, self.win_y+tmpy*25, 25, 25)
        tile = (self.win_x+x*25, self.win_y+y*25, 25, 25)
        self._moving_dir = y-tmpy + 2*(x-tmpx)
        self._skin = skin % 4
        self._player_x, self._player_y = x, y
        match mapelement:
            case 0:
                self._screen.fill(BLACK, old_tile)
            case 5:
                if bluepu:
                    self._screen.fill(BLUE_DIM, old_tile)
                else:
                    self._screen.fill(BLUE, old_tile)
            case 7:
                if orangepu:
                    self._screen.fill(ORANGE_DIM, old_tile)
                else:
                    self._screen.fill(ORANGE, old_tile)
            case 9:
                if magentapu:
                    self._screen.fill(MAGENTA_DIM, old_tile)
                else:
                    self._screen.fill(MAGENTA, old_tile)
            case _:
                raise Exception("draw player map element exception")
        pygame.display.update(old_tile)
        p = get_image(f"assets\\player\\{self._skin}skin3.png")
        match self._moving_dir:
            case 1:
                p = pygame.transform.rotate(p, -90)
            case -1:
                p = pygame.transform.rotate(p, 90)
            case 2:
                pass
            case -2:
                p = pygame.transform.rotate(p, 180)
        self._screen.fill(BLACK, tile)
        self._screen.blit(p, tile)
        pygame.display.update(tile)
        self._ticks = 0

    def tick(self, end=0):
        if end == 1:
            return
        elif end == 2:
            self._animate_win()
            self._ticks += 1
            return
        self._player_anim()
        self._ticks += 1

    def _player_anim(self):
        p = None
        tile = (self.win_x + self._player_x*25, self.win_y + self._player_y*25, 25, 25)
        if self._ticks % 30 == 0:
            p = get_image(f"assets\\player\\{self._skin}skin1.png")
        elif self._ticks % 15 == 0:
            p = get_image(f"assets\\player\\{self._skin}skin2.png")
        else:
            return
        match self._moving_dir:
            case 1:
                pass
            case -1:
                p = pygame.transform.rotate(p, 180)
            case 2:
                p = pygame.transform.rotate(p, 90)
            case -2:
                p = pygame.transform.rotate(p, -90)
        self._screen.fill(BLACK, tile)
        self._screen.blit(p, tile)
        pygame.display.update(tile)

    #  Metoda przerysowujaca statystki gry (czas, power-upy)
    def update_stats(self, game_time, bluepu, orangepu, magentapu, level_name):
        self._screen.fill(BLACK, (self.stats_x, self.stats_y, self.stats_width, self.stats_height))
        text = self._font.render(level_name, True, YELLOW, BLACK)
        name_width = text.get_rect().width
        self._screen.blit(text, (self.stats_x+20, self.stats_y+self.stats_height/2-18))
        text = self._font.render("POWER-UPS:", True, YELLOW, BLACK)
        self._screen.blit(text, (self.stats_x+name_width + 50, self.stats_y+self.stats_height/2-18))
        pb, po, pm = None, None, None
        if bluepu:
            pb = pygame.transform.scale(get_image("assets\\power\\b-power-blue.png"), (32, 32))
        else:
            pb = pygame.transform.scale(get_image("assets\\power\\b-power-blue-dim.png"), (32, 32))
        if orangepu:
            po = pygame.transform.scale(get_image("assets\\power\\b-power-orange.png"), (32, 32))
        else:
            po = pygame.transform.scale(get_image("assets\\power\\b-power-orange-dim.png"), (32, 32))
        if magentapu:
            pm = pygame.transform.scale(get_image("assets\\power\\b-power-magenta.png"), (32, 32))
        else:
            pm = pygame.transform.scale(get_image("assets\\power\\b-power-magenta-dim.png"), (32, 32))

        tmp = [pb, po, pm]
        for i in range(len(tmp)):
            self._screen.blit(tmp[i], (self.stats_x+name_width + 50+text.get_rect().width+32*i+8*(i+1), self.stats_y+self.stats_height/2-16))

        text = self._font.render(f"TIME: {game_time}", True, YELLOW, BLACK)
        self._screen.blit(text, (self.stats_x + 510, self.stats_y + self.stats_height / 2 - 18))
        pygame.display.update((self.stats_x, self.stats_y, self.stats_width, self.stats_height))

        if self._skin == -1:
            return
        self._player_anim()

    #  Metoda rysujaca okno gry
    def _draw(self):
        self._screen.fill(BLACK)
        self._draw_title("logicagent-trans-dim.png")
        self._draw_borders()
        self._draw_level()

    #  Metoda rysujaca przyciemniony tytul
    def _draw_title(self, title_name):
        title_image = get_image(f"assets\\{title_name}")
        title_image = pygame.transform.scale(title_image, TITLE_SIZE)
        rect = title_image.get_rect()
        rect.center = (self._s_width / 2, rect.height / 2 + 30)
        self._screen.fill(BLACK, rect)
        self._screen.blit(title_image, rect)
        pygame.display.update(rect)

    #  Metoda wybierjaca wariant ekranu koncowego
    def endgame(self, end_type):
        self._screen.fill(BLACK)
        if end_type == 1:
            self._draw_endgame_lost()
        else:
            self._draw_endgame_win()
        pygame.display.update()

    #  Metoda rysujaca ekran koncowy - przegrana
    def _draw_endgame_lost(self):
        pygame.draw.rect(self._screen, RED, (0, 0, self._s_width, self._s_height), 2)
        pygame.draw.rect(self._screen, RED, (6, 6, self._s_width - 12, self._s_height - 12), 2)
        self._draw_title("deadagent-half.png")
        text1 = self._font.render("YOU LOST", True, RED, BLACK)
        text2 = self._font.render("PRESS ENTER/SPACE TO CONTINUE", True, RED, BLACK)
        rect = text1.get_rect()
        rect.center = (self._s_width/2, 488)
        self._screen.blit(text1, rect)
        pygame.display.update(rect)
        rect = text2.get_rect()
        rect.center = (self._s_width / 2, 530)
        self._screen.blit(text2, rect)
        pygame.display.update(rect)

    def _animate_win(self):
        if self._ticks % 60 == 0:
            self._draw_title("logicagent-trans.png")
        elif self._ticks % 30 == 0:
            self._draw_title("logicagent-half.png")


    #  Metoda rysujaca ekran koncowy - zwyciestwo
    def _draw_endgame_win(self):
        pygame.draw.rect(self._screen, YELLOW, (0, 0, self._s_width, self._s_height), 2)
        pygame.draw.rect(self._screen, YELLOW, (6, 6, self._s_width - 12, self._s_height - 12), 2)
        self._draw_title("logicagent-half.png")
        text1 = self._font.render("YOU WON :)", True, YELLOW, BLACK)
        text2 = self._font.render("PRESS ENTER/SPACE TO CONTINUE", True, YELLOW, BLACK)
        rect = text1.get_rect()
        rect.center = (self._s_width / 2, 488)
        self._screen.blit(text1, rect)
        pygame.display.update(rect)
        rect = text2.get_rect()
        rect.center = (self._s_width / 2, 530)
        self._screen.blit(text2, rect)
        pygame.display.update(rect)

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
        for y in range(13):
            for x in range(26):
                # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
                # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
                img = None
                tile = (self.win_x+x*25, self.win_y+y*25, 25, 25)
                match self._level[y][x]:
                    case 0:
                        self._screen.fill(BLACK, tile)
                    case 1:
                        self._screen.fill(WHITE, tile)
                    case 2:
                        img = get_image("assets\\exit.png")
                    case 3:
                        img = get_image("assets\\enemy.png")
                    case 4:
                        img = get_image("assets\\power\\s-power-blue.png")
                    case 5:
                        self._screen.fill(BLUE, tile)
                    case 6:
                        img = get_image("assets\\power\\s-power-orange.png")
                    case 7:
                        self._screen.fill(ORANGE, tile)
                    case 8:
                        img = get_image("assets\\power\\s-power-magenta.png")
                    case 9:
                        self._screen.fill(MAGENTA, tile)
                if img is not None:
                    self._screen.blit(img, tile)
        pygame.display.update((self.win_x, self.win_y, self.win_width, self.win_heigth))

    #  Metoda przerysowujaca elementy mapy zmieniajace sie w trakcie gry (kolorowe sciany, power-upy)
    def redraw_level(self, bluepu, orangepu, magentapu):
        for y in range(13):
            for x in range(26):
                # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
                # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
                tile = (self.win_x + x * 25, self.win_y + y * 25, 25, 25)
                match self._level[y][x]:
                    case 5:
                        if bluepu:
                            self._screen.fill(BLUE_DIM, tile)
                    case 7:
                        if orangepu:
                            self._screen.fill(ORANGE_DIM, tile)
                    case 9:
                        if magentapu:
                            self._screen.fill(MAGENTA_DIM, tile)
                pygame.display.update(tile)

    def direction_from_mouse(self, x, y):
        x = x*25+12+self.win_x
        y = y*25+12+self.win_y
        mx, my = pygame.mouse.get_pos()
        if abs(mx-x) > abs(my-y):
            if mx-x >= 0:
                return "RIGHT"
            return "LEFT"
        if my-y >= 0:
            return "DOWN"
        return "UP"

    def refresh(self):
        pass
