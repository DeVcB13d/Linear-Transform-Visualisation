import pygame as pg
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
        pygame UI equialent values
        """
        return tuple([self.win_len/2+inx,self.win_wid/2+iny])

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

        
    







