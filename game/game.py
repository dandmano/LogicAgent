import numpy as np
from game.level import Level
from game.states import *

TER_LINES = 20
TER_COLS = 55

S_MENU = 10
S_PLAY = 0
S_LEVEL_EDITOR = 1
S_SETTINGS = 2
S_EXIT = 3


class Game:

    _difficulty = 1  # 0 - easy 1 - normal 2 - hard

    def __init__(self, gui):
        self._state = S_MENU  # initial state = menu
        self._levels = []
        self._load_levels()
        self._gui = gui

    def loop(self):
        while self._state != 3:
            new_state = 10  # Menu
            match self._state:
                case 10:  # Menu
                    state_menu = StateMenu(self._gui)
                    new_state = state_menu.loop_menu()
                case 0:  # Play
                    raise Exception("Play")
                case 1:  # Level Editor
                    raise Exception("Level Editor")
                case 2:  # Settings
                    raise Exception("Settings")
                case 3:  # Exit
                    return
            self._state = new_state

    def _load_levels(self):  # temporary
        level = Level("Level 1", None)
        self._levels.append(level.level)
