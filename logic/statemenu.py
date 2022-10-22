from logic.audio import _sound_library
from logic.audio import play_sound

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
                    play_sound("audio\\beep.mp3")
                case "KEY_DOWN":
                    selected_el += 1
                    play_sound("audio\\beep.mp3")
                case " ":
                    play_sound("audio\\confirm.mp3")
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
                    play_sound("audio\\beep.mp3")
                case "KEY_DOWN":
                    selected_el += 1
                    play_sound("audio\\beep.mp3")
                case " ":
                    if selected_el == 3:
                        play_sound("audio\\confirm.mp3")
                        return difficulty
                    play_sound("audio\\confirm.mp3")
                    difficulty = selected_el
                    self._gui.menu.current_difficulty_change(difficulty)
                case _:
                    continue
            selected_el %= 4
            self._gui.menu.sel_el_changed_difficulty(selected_el)
            self._gui.menu.refresh()

    def loop_skin(self, skin):
        sel_skin = skin
        snumber = 7
        self._gui.menu.print_skin_menu()
        self._gui.menu.sel_skin_changed_skin((sel_skin-1) % snumber, sel_skin, (sel_skin+1) % snumber)
        self._gui.menu.refresh()
        key = None
        while key != 'q':
            try:
                key = self._gui.getkey()
            except Exception:
                key = None
                continue
            match key:
                case "KEY_LEFT":
                    sel_skin -= 1
                    play_sound("audio\\beep.mp3")
                case "KEY_RIGHT":
                    sel_skin += 1
                    play_sound("audio\\beep.mp3")
                case " ":
                    play_sound("audio\\confirm.mp3")
                    return sel_skin
                case None:
                    continue
            sel_skin %= snumber
            self._gui.menu.sel_skin_changed_skin((sel_skin-1) % snumber, sel_skin, (sel_skin+1) % snumber)

    def loop_level(self, levels):
        sel_level = 0
        lnr = len(levels)
        self._gui.menu.print_level_menu()
        self._gui.menu.sel_level_changed(levels, (sel_level-1) % lnr, sel_level, (sel_level+1) % lnr)
        key = None
        while key != 'q':
            try:
                key = self._gui.getkey()
            except Exception:
                key = None
                continue
            match key:
                case "KEY_UP":
                    sel_level -= 1
                    play_sound("audio\\beep.mp3")
                case "KEY_DOWN":
                    sel_level += 1
                    play_sound("audio\\beep.mp3")
                case " ":
                    play_sound("audio\\confirm.mp3")
                    return sel_level
                case None:
                    continue
            sel_level %= lnr
            self._gui.menu.sel_level_changed(levels, (sel_level - 1) % lnr, sel_level, (sel_level + 1) % lnr)
