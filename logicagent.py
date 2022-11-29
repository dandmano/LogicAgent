from curses import wrapper

from gui.gui import Gui
from logic.logic import Logic
from textgui.tgui import TGui


#  Funkcja glowna programu, tworzy obiekt gui i logiki oraz rozpoczyna petle
def main(stdscr):
    if stdscr is None:
        gui = Gui()
    else:
        gui = TGui(stdscr)
    logic = Logic(gui)
    logic.loop()


textgui = False

if textgui:
    wrapper(main)
elif __name__ == "__main__":
    main(None)

