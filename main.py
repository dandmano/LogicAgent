from textgui.tgui import TGui
from game.game import Game
from curses import wrapper

def main(stdscr):
    gui = TGui(stdscr)
    game = Game(gui)
    game.loop()

wrapper(main)

