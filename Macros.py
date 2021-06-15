"""
Contains all the important macros
"""

import pygame

# (0,0) = Top Left Corner
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size)

GAME_NAME = "TIC TAC TOE"
pygame.display.set_caption(GAME_NAME)

background = pygame.Surface(screen.get_size())
background_image = pygame.image.load("images/Bamboo_bc_1.bmp").convert()
x_mark = pygame.image.load("images/Player_X.png").convert_alpha()
o_mark = pygame.image.load("images/Player_O.png").convert_alpha()
