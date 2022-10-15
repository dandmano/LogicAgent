from game.level import Level
from game.states import *

TER_LINES = 22
TER_COLS = 58

S_MENU = 0
S_GAME = 1
S_DIFFICULTY = 2


class Game:

    _difficulty = 1  # 0 - easy 1 - normal 2 - hard

    def __init__(self, gui):
        self._state = S_MENU  # initial state = menu
        self._levels = []
        self._load_levels()
        self._gui = gui

    def loop(self):
        state_menu = StateMenu(self._gui)
        while self._state != 3:
            new_state = 0  # Menu
            match self._state:
                case 0:  # Menu
                    new_state = state_menu.loop_menu()
                case 1:  # Play
                    state_play = StatePlay(self._gui, self._difficulty, self._levels[0])
                    new_state = state_play.loop()
                case 2:  # Difficulty
                    self._difficulty = state_menu.loop_difficulty(self._difficulty)
                case 3:  # Exit
                    return
            self._state = new_state

    def _load_levels(self):  # temporary
        level = Level("Level 1", None)
        self._levels.append(level.level)
