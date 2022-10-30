from textgui.tgui import TGui
from logic.logic import Logic
from curses import wrapper


def main(stdscr):
    gui = TGui(stdscr)
    logic = Logic(gui)
    logic.loop()


wrapper(main)
