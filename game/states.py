
class StatePlay:
    def __init__(self, gui, difficulty, level):
        if difficulty == 1:
            self._lives = 3
        else:
            self._lives = 1
        self._level = level
        self._gui = gui
        self._difficulty = difficulty

    def loop(self):
        game_gui = self._gui.new_game(self._level)
        player_x, player_y = 0, 1
        tmp_x, tmp_y = 0, 1
        player_pos = 0  # 0 - up 1 - down 2 - left 3 - right
        game_gui.draw_player(tmp_x, tmp_y, player_x, player_y, player_pos)
        key = None
        while key != "q":
            try:
                key = self._gui.getkey()
            except:
                key = None
                continue
            match key:
                case "KEY_UP":
                    if player_y - 1 > 0:
                        player_y -= 1
                        player_pos = 1
                case "KEY_DOWN":
                    if player_y + 1 < 11:
                        player_y += 1
                        player_pos = 0
                case "KEY_LEFT":
                    if player_x - 1 > 0:
                        player_x -= 1
                        player_pos = 3
                case "KEY_RIGHT":
                    if player_x + 1 < 19:
                        player_x += 1
                        player_pos = 2
                case "q":
                    break
                case _:
                    continue
            game_gui.draw_player(tmp_x, tmp_y, player_x, player_y, player_pos)
            tmp_y = player_y
            tmp_x = player_x
        return 3  # quit






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

