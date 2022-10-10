import curses as cs
from textgui.tgui import TGui
from game.game import Game
from curses import wrapper


def main(stdscr):
    # game = Game()
    # curr_level = game.levels[0]
    # print(f'{curr_level[0][0]} + dalej + {curr_level[1][1]} + dalej + {curr_level[7][4]}')
    gui = TGui(stdscr)
    gui.display_menu()
    stdscr.getch()

wrapper(main)

