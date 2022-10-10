class StateMenu:
    _elements = [0, 1, 2, 3]  # 0 - play 1 - create level 2 - settings 3 - quit

    def __init__(self, gui):
        self._gui = gui
        self._gui.menu.refresh()

    def loop(self):
        selected_el = 0
        self._gui.menu.sel_el_changed(selected_el)
        self._gui.menu.refresh()
        key = None
        while key != "q":
            try:
                key = self._gui.getkey()
            except:
                key = None
                continue
            match key:
                case "KEY_UP":
                    selected_el -= 1
                case "KEY_DOWN":
                    selected_el += 1
                case " ":
                    return selected_el
                case _:
                    continue
            selected_el %= 4
            self._gui.menu.sel_el_changed(selected_el)
            self._gui.menu.refresh()
        return 3  # quit
