import time

from logic.audiologic import play_sound, change_sound_on
from pygame.time import Clock


#  Klasa stanu menu, ktora obsluguje glowne menu, opcje wyboru skina, levelu, poziomu trudnosci oraz wyciszanie gry
class StateMenu:
    def __init__(self, gui):
        self._gui = gui
        self._clock_fps = Clock()

    #  Petla obslugujaca menu (inputy, wybory)
    def loop_menu(self):
        selected_el = 0
        self._gui.menu.print_main_menu()
        self._gui.menu.sel_el_changed_menu(selected_el)
        self._gui.menu.refresh()
        key = None
        while key != "q":
            self._clock_fps.tick(30)
            self._gui.menu.tick()
            try:
                key = self._gui.getkey()
            except Exception:
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
                case "m":
                    change_sound_on()
                case "quit":
                    quit(0)
                case _:
                    continue
            selected_el %= 4
            self._gui.menu.sel_el_changed_menu(selected_el)
            self._gui.menu.refresh()
        return 3  # quit

    # Petla obsuguljaca wybor poziomu trudnosci
    def loop_difficulty(self, difficulty):
        selected_el = 0
        self._gui.menu.print_difficulty_menu()
        self._gui.menu.sel_el_changed_difficulty(selected_el)
        self._gui.menu.current_difficulty_change(difficulty)
        self._gui.menu.refresh()
        key = None
        while key != "q":
            self._clock_fps.tick(30)
            self._gui.menu.tick()
            try:
                key = self._gui.getkey()
            except Exception:
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
                case "quit":
                    quit(0)
                case _:
                    continue
            selected_el %= 3
            self._gui.menu.sel_el_changed_difficulty(selected_el)
            self._gui.menu.refresh()
        return difficulty

    #  Petla obslugujaca menu wyboru skina
    def loop_skin(self, skin):
        sel_skin = skin
        snumber = 8
        self._gui.menu.print_skin_menu()
        self._gui.menu.sel_skin_changed_skin((sel_skin - 1) % snumber, sel_skin, (sel_skin + 1) % snumber)
        self._gui.menu.refresh()
        key = None
        while key != 'q':
            self._clock_fps.tick(30)
            self._gui.menu.tick()
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
                case "quit":
                    quit(0)
                case None:
                    continue
            sel_skin %= snumber
            self._gui.menu.sel_skin_changed_skin((sel_skin - 1) % snumber, sel_skin, (sel_skin + 1) % snumber)
        return sel_skin

    #  Petla obslugujaca menu wyboru levela
    def loop_level(self, levels):
        sel_level = 0
        lnr = len(levels)
        self._gui.menu.print_level_menu()
        self._gui.menu.sel_level_changed(levels, (sel_level - 1) % lnr, sel_level, (sel_level + 1) % lnr)
        key = None
        while key != 'q':
            self._clock_fps.tick(30)
            self._gui.menu.tick()
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
                case "quit":
                    quit(0)
                case None:
                    continue
            sel_level %= lnr
            self._gui.menu.sel_level_changed(levels, (sel_level - 1) % lnr, sel_level, (sel_level + 1) % lnr)
        return -1
