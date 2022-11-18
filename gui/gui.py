import pygame


#  Glowna klasa interfejsu graficznego. Inicjalizuje interfejs (curses), jego okna i podokna oraz kolory
class Gui:

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Logic Agent")
        self._font = pygame.font.Font("assets\\VIDEOPHREAK.ttf", 14)
        pygame.display.set_icon(pygame.image.load("assets\\icon.png"))



    def menu(self):
        return self._menu_gui

    def game(self):
        return self._game_gui


    def _init_menu(self):
        self._menu_win = None
        self._menu_gui = None

    def _init_game_map(self, level):
        self._game_gui = None

    def new_game(self, level):
        self._init_game_map(level)
        return self._game_gui

    def getkey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                return self._keys(event.key)
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


