from logic.level import Level
from logic.statemenu import StateMenu
from logic.stategame import StateGame

TER_LINES = 22
TER_COLS = 58

S_MENU = 10
S_GAME = 0
S_CREATE_LEVEL = 1
S_DIFFICULTY = 2

class Logic:

    _difficulty = 1  # 0 - easy 1 - normal 2 - hard

    def __init__(self, gui):
        self._state = S_MENU  # initial state = menu
        self._levels = []
        self._load_levels()
        self._gui = gui

    def loop(self):
        state_menu = StateMenu(self._gui)
        while self._state != 3:
            new_state = 10  # Menu
            match self._state:
                case 10:  # Menu
                    new_state = state_menu.loop_menu()
                case 0:  # Play
                    state_game = StateGame(self._gui, self._difficulty, self._levels[0])
                    state_game.loop()
                case 1:  # Difficulty
                    self._difficulty = state_menu.loop_difficulty(self._difficulty)
                case 2:  # Create Level
                    raise Exception("Create Level")
                case 3:  # Exit
                    return
            self._state = new_state

    def _load_levels(self):  # temporary
        level = Level("Level 1", None)
        self._levels.append(level.level)
