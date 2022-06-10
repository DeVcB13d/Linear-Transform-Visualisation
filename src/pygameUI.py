import pygame, sys
from graph import *

# CONSTANTS
BLUE = (0, 0, 51)
YELLOW = (255, 255, 0)
LAV = (229, 204, 255)
wind_len = 500
wind_brea = 500
grid_line_width = 3
pygame.init()
# SCREEN
screen = pygame.display.set_mode((wind_len, wind_brea))
pygame.display.set_caption('Linear transformation')
screen.fill(BLUE)
pygame_icon = pygame.image.load('media\logo.jpg')
pygame.display.set_icon(pygame_icon)


def main():
    run = True
    Plane = Coordinate_plane(screen,wind_len,wind_brea,wind_len/10)
    plt = Plotter(screen,Plane)
    plt.plot(200,100)
    plt.plot(400,-205)
    #draw_line()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                run = False
        pygame.display.update()


main()
