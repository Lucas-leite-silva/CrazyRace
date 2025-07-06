from entity import Entity
import pygame

class Oil(Entity):
    def __init__(self, position: tuple):
        super().__init__('Oil', position)
        self.debuff_duration = 180
        self.active_debuff_on_player = {None: False}
        self.hit_this_frame = False

    def move(self):
        pass

    def on_collide(self, player):
        if not self.active_debuff_on_player.get(player, False):
            player.original_speed = player.speed
            player.speed /= 2
            self.active_debuff_on_player[player] = True
            player.debuff_timer = self.debuff_duration
            print(f"Jogador {player.name} passou no Óleo!")