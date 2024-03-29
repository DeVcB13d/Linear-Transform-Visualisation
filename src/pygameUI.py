import pygame, sys
from graph import *
from constants import *
# CONSTANTS

# SCREEN

'''
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
'''

def run():
    screen = pg.display.set_mode((WIN_LEN,WIN_WID))
    pg.display.set_caption('Linear transformation')
    screen.fill(BLUE)
    pg_icon = pg.image.load('media\logo.jpg')
    pg.display.set_icon(pg_icon)
    run = True
    Plane = Coordinate_plane(screen)
    #plt = Plotter(screen,Plane)
    #draw_line()
    while run:
        keys = pg.key.get_pressed()
        if (keys[pg.K_a]):
            Plane.clear_screen()
            p1 = eval(input("Enter Transform Matrix : "))
            Plane.transform(p1[0],p1[1])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                run = False
            if (event.type == pg.MOUSEBUTTONUP):
                # To print the selected coordinate
                pos = pg.mouse.get_pos()
                Plane.clear_screen()
                a,b = Plane.rev_coordinate(pos[0],pos[1])
                print(approx(a),approx(b))
            #if (event.type == pg.K_SPACE):
                #base1 = eval(input("Enter base 1 : "))
                #base2 = (0,1)
                #Plane.draw_grid_new_base(base1,base2)
                #p1 = eval(input("Enter Transform Matrix : "))
                #p2 = eval(input("Enter point 2 : "))
                #Plane.transform(p1[0],p1[1])
                
                #Plane.draw_line((3,4),(2,1),5,PINK)
        pg.display.update()   

run()