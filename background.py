from Const import WIN_WIDTH
from entity import Entity
import pygame

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = 3

    def move(self):
        pass