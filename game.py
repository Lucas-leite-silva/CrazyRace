# game.py
import pygame

from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Crazy Race")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
               level = Level(self.window, 'Level1', menu_return)
               level_return = level.run()
               if level_return == "menu":
                   continue

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            else:
                pass