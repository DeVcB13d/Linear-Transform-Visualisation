import pygame as pg
import sys
from constants import *

class Coordinate_plane:

    def __init__(self,screen,win_len,win_wid,thick = 100):
        self.screen = screen
        self.win_len = win_len
        self.win_wid = win_wid
        self.thick = thick
        self.draw_grid(self.thick)
        self.draw_axis()
        
    def coordinate(self,inx,iny):
        """
        To input the coodinates and return its 
        pg UI equialent values
        """
        return tuple([self.win_len/2+inx,self.win_wid/2+iny])
    def rev_coordinate(self,inx,iny):
        '''
        To return the cartesian values from pg values
        '''
        return tuple([inx - self.win_len/2 + 1,iny - self.win_wid/2 -1])
    def draw_grid(self,gridsize,line_t = 4):
        '''
        To draw the main grid with each line spaced by gridsize
        '''
        posX = self.win_wid/2
        pg.draw.line(self.screen, YELLOW, (posX,0), (posX,self.win_len),line_t)
        posY = self.win_len/2
        pg.draw.line(self.screen, YELLOW, (0, posY), (self.win_wid, posY),line_t)
        # Drawing vertical lines
        vert_ini_pos = [0, 0]
        vert_fin_pos = [0, self.win_len]
        hor_ini_pos = [0, 0]
        hor_fin_pos = [self.win_wid, 0]
        for i in range(1, self.win_len // 10 + 2):
            pg.draw.line(self.screen, LAV, vert_ini_pos, vert_fin_pos,line_t)
            vert_ini_pos[0] += gridsize
            vert_fin_pos[0] += gridsize
        for i in range(1, self.win_wid // 10 + 2):
            pg.draw.line(self.screen, LAV, hor_ini_pos, hor_fin_pos,line_t)
            hor_ini_pos[1] += gridsize
            hor_fin_pos[1] += gridsize
    def draw_axis(self):
        """
        To draw the coordinate axes
        """
        posX =self.win_wid/2
        pg.draw.line(self.screen, YELLOW, (posX,0), (posX,self.win_len), 2)
        posY = self.win_len/2
        pg.draw.line(self.screen, YELLOW, (0, posY), (self.win_wid, posY), 2)

    # TO zoom the system by the ratio 
    def zoom(ratio):
        pass
        

class Plotter:
    '''
    To plot the vectors onto the graph
    '''
    def __init__(self,screen,plane):
        self.screen = screen
        self.plane = plane
    def plot(self,x,y):
        start = self.plane.coordinate(0,0)
        end = self.plane.coordinate(x,y) 
        pg.draw.line(self.screen,(0,0,255),start,end,4)

        
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

        pg.display.update()   
    
run()





