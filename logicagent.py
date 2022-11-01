from textgui.tgui import TGui
from logic.logic import Logic
from curses import wrapper

#  Funkcja glowna programu, tworzy obiekt gui i logiki oraz rozpoczyna petle
def main(stdscr):
    gui = TGui(stdscr)
    logic = Logic(gui)
    logic.loop()


wrapper(main)
