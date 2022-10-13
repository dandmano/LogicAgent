class StateMenu:
    _menu_elements = [0, 1, 2, 3]  # 0 - play 1 - create level 2 - settings 3 - quit
    _settings_elements = [0, 1, 2]  # 0 - main color 1 - difficulty 2 - return
    _color_elements = [0, 1, 2, 3]  # 0 - current 1 - yellow 2 - purple 3 - return
    _difficulty_elements = [0, 1, 2, 3]  # 0 - current 1 - easy 2 - hard 3 - return

    MENU = 0
    SETTINGS = 1
    MAIN_COLOR = 2
    DIFFICULTY = 3

    def __init__(self, gui):
        self._gui = gui
        self._gui.menu.refresh()

    def loop_menu(self):
        sel = self._universal_loop(self.MENU, self._menu_elements)
        if sel == 3:
            return sel

    def _universal_loop(self, option, elements):
        selected_el = 0
        self._gui.menu.sel_el_changed(selected_el, option)
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
            selected_el %= len(elements)
            self._gui.menu.sel_el_changed(selected_el, option)
            self._gui.menu.refresh()
        return 3  # quit
