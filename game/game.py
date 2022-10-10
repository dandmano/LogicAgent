import numpy as np
from game.level import Level
from game.states import State


class Game:

    def __init__(self, gui):
        self._state = State.MENU  # initial state = menu
        self._levels = []
        self._load_levels()
        self._gui = gui

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if new_state is not State:
            raise TypeError("new_state is not State type")
        self._state = new_state

    @property
    def levels(self):
        return self._levels

    def loop(self):
        pass

    def _load_levels(self):  # temporary
        level = Level("Level 1", None)
        self._levels.append(level.level)
