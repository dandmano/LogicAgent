import pygame

from gui.views import *

S_WIDTH = 800
S_HEIGHT = 600


#  Glowna klasa interfejsu graficznego. Inicjalizuje interfejs (curses), jego okna i podokna oraz kolory
class Gui:

    def __init__(self):
        pygame.init()
        self.is_graphic = True
        self._screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        pygame.display.set_caption("Logic Agent")
        self._font = pygame.font.Font("assets\\Square.ttf", 34)
        pygame.display.set_icon(pygame.image.load("assets\\icon.png"))
        self._menu = Menu(self._screen, self._font, S_WIDTH, S_HEIGHT)
        self._game = None

    @property
    def menu(self):
        return self._menu

    def game(self):
        return self._game

    def _init_game_map(self, level):
        self._game = Game(self._screen, self._font, S_WIDTH, S_HEIGHT, level)

    def new_game(self, level):
        self._init_game_map(level)
        return self.game()

    def getkey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                return self._keys(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return "mouse_clicked"
        raise Exception("key not pressed")

    def _keys(self, key):
        match key:
            case pygame.K_UP:
                return "KEY_UP"
            case pygame.K_DOWN:
                return "KEY_DOWN"
            case pygame.K_LEFT:
                return "KEY_LEFT"
            case pygame.K_RIGHT:
                return "KEY_RIGHT"
            case pygame.K_SPACE:
                return " "
            case pygame.K_RETURN:
                return " "
            case pygame.K_q:
                return "q"
            case pygame.K_m:
                return "m"
            case _:
                raise Exception("key not found")


