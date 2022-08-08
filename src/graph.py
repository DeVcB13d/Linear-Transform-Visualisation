import pygame as pg
import sys
from constants import *

class Coordinate_plane:

    def __init__(self,screen,win_len,win_wid,grid_size = 10):
        self.screen = screen
        self.win_len = win_len
        self.win_wid = win_wid
        self.grid_size = grid_size
        self.draw_grid(self.grid_size)
        self.draw_axis()
        
    def coordinate(self,inx,iny):
        """
        To input the coodinates and return its 
        pygame UI equialent values
        """
        return tuple([self.win_len/2+inx,self.win_wid/2+iny])
    def rev_coordinate(self,inx,iny):
        '''
        To return the cartesian values from pg values
        '''
        return tuple([self.win_len/2 - inx,self.win_wid/2 - iny])
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
    def draw_grid_new_base(self,base1,base2):
        '''
        Function to draw a new grid based on base1 and base2

        Basic idea 
        >>> We need the start and end points of the line in pygame to draw a line
        >>> To get the equation of the line, we consider 2 points
        >>> Base point : Starts with (0,0) moves up and down by certain units
        >>> Basis point : The coordinates of base 1 and 2
        >>> By using a base point and basis point, we can find the end points
        >>> To find the end points, we either know the x and y coordinate - 
            the length and breadth
        >>> Using the known points, we will be able to find the 2 required endpoints and draw a line
        >>> Hoping to change the direct calculations to matrix multiplication
        '''
        BasePoint = (0,0)
        BasisPoint = base1
        top_x = wind_brea / 2 
        end_x = -top_x
        try:
            top_y = (BasisPoint[1] - BasePoint[1])/(BasisPoint[0] - BasePoint[0]) * (top_x - 0 ) + BasePoint[1];
            end_y = (BasisPoint[1] - BasePoint[1])/(BasisPoint[0] - BasePoint[0]) * (end_x - 0 ) + BasePoint[1];
            end = self.coordinate(top_x,top_y)
            top = self.coordinate(end_x,end_y)
        except:
            pass
        print((top_x,top_y),(end_x,end_y))
        for i in range(0,10):
            top1 = top;top2 = top;end1 = end;end2 = end;
            top1 = (top[0],top[1] + 80*i)
            end1 = (end[0],end[1] + 80*i)
            top2 = (top[0],top[1] - 80*i)
            end2 = (end[0],end[1] - 80*i)
            pg.draw.line(self.screen, PINK,top1,end1,5)
            pg.draw.line(self.screen, PINK,top2,end2,5)
    # TO zoom the system by the ratio 
    def move():
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
            if (event.type == pg.KEYDOWN):
                base1 = eval(input("Enter base 1 : "))
                base2 = (0,1)
                Plane.draw_grid_new_base(base1,base2)

        pg.display.update()   



run()





