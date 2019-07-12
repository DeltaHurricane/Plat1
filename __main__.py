# Jogo em pg teste inicial e possívelmente versão demo futura


import pygame as pg
from classe_Game import Game
import random


def main():

    g = Game()
    g.show_start_screen()
    while g.running == True:
        g.new()
        g.show_go_screen()
    pg.quit


if __name__ == "__main__":
    main()

