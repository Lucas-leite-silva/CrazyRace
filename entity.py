import pygame
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        try:
            self.surf = pygame.image.load('./asset1/' + name + '.png').convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar imagem para {name}: {e}")
            self.surf = pygame.Surface((50, 50))
            self.surf.fill((255, 0, 255))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass

    def on_collide(self, other_entity):
        pass