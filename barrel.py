from entity import Entity
import pygame


class Barrel(Entity):
    def __init__(self, position: tuple):
        super().__init__('Barrel01', position)

    def move(self):
        pass

    def on_collide(self, player):
        if player.rect.centerx < self.rect.centerx:
            player.rect.x -= 10
        else:
            player.rect.x += 10

        print(f"Jogador {player.name} colidiu com o Barril!")