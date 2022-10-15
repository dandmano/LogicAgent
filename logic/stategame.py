import time


class StateGame:
    def __init__(self, gui, difficulty, level):
        self._player_y = None
        self._player_x = None
        self._lives = 3 - difficulty
        self._level = level
        self._gui = gui
        self._game_gui = self._gui.new_game(self._level)
        self._player_moving = False
        self._difficulty = difficulty
        self._bluepu=False
        self._orangepu=False
        self._magentapu=False

    def loop(self):
        self._player_x, self._player_y = self._find_player_spawn()  # actual player cords
        if self._player_x == -1 or self._player_y == -1:
            raise Exception("Player spawn not found!")
        # game_gui.draw_player(tmp_x, tmp_y, player_x, player_y)
        key = None
        while key != "q":
            try:
                key = self._gui.getkey()
            except:
                key = None
                continue
            if self._player_moving:
                continue
            match key:
                case "KEY_UP":
                    self._player_move(self._player_x, self._player_y - 1)
                case "KEY_DOWN":
                    self._player_move(self._player_x, self._player_y + 1)
                case "KEY_LEFT":
                    self._player_move(self._player_x - 1, self._player_y)
                case "KEY_RIGHT":
                    self._player_move(self._player_x + 1, self._player_y)
                case "q":
                    return
                case _:
                    continue

    def _player_move(self, x, y):
        # 0-empty space, 1-wall, 2-exit, 3-spikes, 99 - start pos
        # 4-blue power up, 5-blue wall, 6-orange power up, 7-orange wall, 8-magenta power up, 9-magenta wall
        tmp = self._level[y][x]
        match tmp:
            case 0:
                self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 1:
                return
            case 2:
                #  tymczasowe
                raise Exception("Wygrales")
            case 3:
                #  tymczasowe
                raise Exception("Umarles")
            case 4:
                self._bluepu=True
                self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 5:
                if self._bluepu:
                    self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 6:
                self._orangepu=True
                self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 7:
                if self._orangepu:
                    self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 8:
                self._magentapu=True
            case 9:
                if self._magentapu:
                    self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case 99:
                self._game_gui.draw_player(self._player_x, self._player_y, x, y)
            case _:
                raise Exception("Match error player move")

        self._player_y = y
        self._player_x = x

    def _find_player_spawn(self):
        for y in range(len(self._level)):
            for x in range(len(self._level[y])):
                if self._level[y][x] == 99:
                    return x, y
        return -1, -1
