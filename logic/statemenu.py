class StateMenu:
    def __init__(self, gui):
        self._gui = gui
        self._gui.menu.refresh()

    def loop_menu(self):
        selected_el = 0
        self._gui.menu.print_main_menu()
        self._gui.menu.sel_el_changed_menu(selected_el)
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
            self._gui.menu.sel_el_changed_menu(selected_el)
            self._gui.menu.refresh()
        return 3  # quit

    def loop_difficulty(self, difficulty):
        selected_el = 0
        self._gui.menu.print_difficulty_menu()
        self._gui.menu.sel_el_changed_difficulty(selected_el)
        self._gui.menu.current_difficulty_change(difficulty)
        self._gui.menu.refresh()
        key = None
        while True:
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
                    if selected_el == 3:
                        return difficulty
                    difficulty = selected_el
                    self._gui.menu.current_difficulty_change(difficulty)
                case _:
                    continue
            selected_el %= 4
            self._gui.menu.sel_el_changed_difficulty(selected_el)
            self._gui.menu.refresh()

