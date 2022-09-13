# Creating a line class to work well with the other classess


from typing import overload
from unittest import removeResult


class line:
    def __init__(self,x1,x2,y1,y2):
        self.slope = self.slope_calc(x1,x2,y1,y2)
        self.y_inter = self.y_inter_calc(x1,x2,y1,y2)
        self.x_inter = -1*self.y_inter / self.slope
    def slope_calc(self,x1,x2,y1,y2):
        if x2 == x1:
            return 99999
        else:
            return (y2 - y1)/(x2 - x1)
    def y_inter_calc(self,x1,x2,y1,y2):
        if x2 == x1:
            return 999999
        else:
            return (y1*x2 - y2*x1)/(x2 - x1)
        #return (y2*x1 - y1*x2)/(y2 - y1)
    def x_inter_calc(self,x1,x2,y1,y2):
        return (y2*x1 - y1*x2)/(y2 - y1)
    # To return x coordinate given a y coordinate
    def get_x(self,y):
        return (y - self.y_inter)/ self.slope
    def get_y(self,x):
        return (self.slope*x + self.y_inter)

