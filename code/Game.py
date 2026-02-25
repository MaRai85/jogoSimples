#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import height_max, width_max
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(height_max, width_max))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

