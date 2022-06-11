import pygame, sys
from graph import *
from constants import *
# CONSTANTS

# SCREEN



def run():
    screen = pygame.display.set_mode((wind_len, wind_brea))
    pygame.display.set_caption('Linear transformation')
    screen.fill(BLUE)
    pygame_icon = pygame.image.load('media\logo.jpg')
    pygame.display.set_icon(pygame_icon)
    run = True
    Plane = Coordinate_plane(screen,wind_len,wind_brea,wind_len/10)
    plt = Plotter(screen,Plane)
    #draw_line()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                run = False
        pygame.display.update()


