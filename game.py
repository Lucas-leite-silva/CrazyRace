#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from asset.PNG.Level_Menu.Const import WIN_WIDTH, WIN_HEIGHT
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        menu = Menu(self.window)
        menu.run()
        pass




