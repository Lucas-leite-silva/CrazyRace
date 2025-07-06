import pygame
from entity import Entity
from Const import WIN_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: tuple, keys: dict):
        super().__init__(name, position)
        self.speed = 5
        self.keys = keys
        self.original_speed = self.speed
        self.debuff_timer = 0

    def update(self):
        if self.debuff_timer > 0:
            self.debuff_timer -= 1
            if self.debuff_timer == 0:
                self.speed = self.original_speed
                self.debuff_timer = 0
        pass

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.keys['right']]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0