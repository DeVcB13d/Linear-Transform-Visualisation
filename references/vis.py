# To build the game from scratch


BLUE = (0, 0, 51)
YELLOW = (255, 255, 0)
LAV = (229, 204, 255)
PINK = (255,204,204)
#INTERFACE CONSTANTS
WIN_LEN = 400
WIN_WID = 400
GRID_LINE_WIDTH = 5
DEFAULT_LINE_THICKNESS = 10

from typing import overload



class line:
    @overload(float,float,float,float)
    def __init__(self,x1,x2,y1,y2):
        # Create a line given 2 points
        pass
    @overload(float,float)
    def __init__(self,m,c):
        # Create a line with slope and abscissa
        pass
    def draw(self,plane):
        # Draw the line onto a plane
        pass
    def remove(self,plane):
        # Remove a line from the plane
        pass
    def customize(self,color = YELLOW,thickness = DEFAULT_LINE_THICKNESS):
        pass
    

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
        BasisPoint = base1 #(1,2)
        top_x = self.win_wid # 200
        end_x = -top_x # -200
        try:
            # ( 1 - 0 / 2 - 0 ) * (200 - 0) + 0  = 100
            top_y = (BasisPoint[1] - BasePoint[1])/(BasisPoint[0] - BasePoint[0]) * (top_x - 0 ) + BasePoint[1];
            # ( 1 - 0 ) -100
            end_y = (BasisPoint[1] - BasePoint[1])/(BasisPoint[0] - BasePoint[0]) * (end_x - 0 ) + BasePoint[1];
            top = self.coordinate(top_x,top_y) #(200,100)
            end = self.coordinate(end_x,end_y) #(-200,-100)
            print("END : ",end,"TOP : ",top)
        except:
            pass
        print((top_x,top_y),(end_x,end_y))
        
        mes_scale = self.scale*((self.win_len/10)*100)
        for i in range(0,10):
            top1 = top;top2 = top;end1 = end;end2 = end;
            top1 = (top[0],top[1] + mes_scale*i)
            end1 = (end[0],end[1] + mes_scale*i)
            end2 = (top[0],top[1] - mes_scale*i)
            top2 = (end[0],end[1] - mes_scale*i)
            pg.draw.line(self.screen,PINK,top1,end1,5)
            pg.draw.line(self.screen,PINK,top2,end2,5)


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