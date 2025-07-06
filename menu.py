#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset1/WindowMaior.png')
        self.rect = self.surf.get_rect(left=0, top=0)



    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()

        # Checa todos eventos
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def menu_text (self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface = text.font.render(text, True, text_color)
        text_rect: Rect = text.surf.get_rect(center=text_center_pos)
        self.window.blit()



