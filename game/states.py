import numpy as np
from enum import Enum


class State(Enum):
    MENU = 1
    GAME = 2
    PAUSE = 3


class StateMenu:
    _elements = [0, 1, 2]  # 0 - play 1 - create level 2 - settings 3 - quit

    def __init__(self, gui):
        self._gui = gui

    def loop(self):
        selected_el = 0
        while key != "q":
            try:
                key = self._gui.getkey()
            except:
                key = None
                continue
            match key:
                case "KEY_UP":
                    selected_el += 1
                case "KEY_DOWN":
                    selected_el -= 1
            selected_el %= 4
            self.gui.menu.sel_el_changed()
