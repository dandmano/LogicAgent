import numpy as np
import time
import curses as cs
from textguistatic import TGStatic as tgs
from textgui import TGui
from curses import wrapper


def main(stdscr):
    gui = TGui(stdscr)
    stdscr.refresh()
    gui.display_menu()
    stdscr.getch()


wrapper(main)

