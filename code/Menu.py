#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import width_max, height_max, VERMELHO, MENU_OPTION, BRANCO


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/Menu_v2.png')
        # Carregando a imagem de fundo do menu
        self.rect = self.surf.get_rect(left=0, top=0)
        # O rectangle vai ter uma imagem

    def run(self, ):
        # INSERINDO A MUSICA
        pygame.mixer_music.load("./assets/dark_intro.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # imagem tem de aparecer no retangulo
            self.menu_texto(50, 'A Ghost Story', VERMELHO, ((height_max / 2), 70))
            self.menu_texto(30, 'The returning', (128, 0, 128), ((height_max / 2), 120))
            # MENU DE JOGO
            for i in range(len(MENU_OPTION)):
                self.menu_texto(20, MENU_OPTION[i], BRANCO, ((height_max / 2), 450 + 50 * i))
            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quiting . . .')
                    pygame.quit()  # close window
                    quit()  # end pygame

    def menu_texto(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
