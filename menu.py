# menu.py
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Const import WIN_WIDTH, C_RED, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset1/WindowMenor.png')
        self.rect = self.surf.get_rect(left=0, top=0)



    def run(self, ):
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, "Crazy", C_RED, ((WIN_WIDTH /2), 90))
            self.menu_text(60, "Race", C_RED, ((WIN_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(60, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 500 + 70 * i))
                else:
                    self.menu_text(60, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 500 + 70 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len (MENU_OPTION):
                            menu_option +=1
                        else: menu_option =0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                             menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text (self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)