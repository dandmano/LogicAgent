import numpy as np
import time
import curses as cs
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(3, 10, "siemacotam")
    stdscr.addstr(4, 10, "siemacotam", cs.A_CHARTEXT)
    stdscr.addstr(5, 10, "siemacotam", cs.A_REVERSE)
    stdscr.addstr(6, 10, "siemacotam", cs.A_INVIS)
    stdscr.addstr(7, 10, "siemacotam", cs.A_BOLD)
    stdscr.addstr(8, 10, "siemacotam", cs.A_STANDOUT)

    stdscr.refresh()
    stdscr.getch()


wrapper(main)

