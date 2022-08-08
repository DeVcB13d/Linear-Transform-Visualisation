import pygame, sys
from graph import *
from constants import *
# CONSTANTS

# SCREEN


def run():
    screen = pg.display.set_mode((wind_len, wind_brea))
    pg.display.set_caption('Linear transformation')
    screen.fill(BLUE)
    pg_icon = pg.image.load('media\logo.jpg')
    pg.display.set_icon(pg_icon)
    run = True
    Plane = Coordinate_plane(screen,wind_len,wind_brea,wind_len/10)
    plt = Plotter(screen,Plane)
    #draw_line()
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                run = False
            if (event.type == pg.MOUSEBUTTONUP):
                # To print the selected coordinate
                pos = pg.mouse.get_pos()
                print(Plane.rev_coordinate(pos[0],pos[1]))
            if (event.type == pg.KEYDOWN):
                base1 = eval(input("Enter base 1 : "))
                base2 = (0,1)
                Plane.draw_grid_new_base(base1,base2)

        pg.display.update()   


