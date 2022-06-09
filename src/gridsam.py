'''
Creating a grid class to represent the grid
> A grid is an abstraction of the vector space
> The standard basic grid is formed by the basis vectors i(0,1) and j(1,0)
> With the basis vectors, we can form a grid which is represented as a set of points in the memory
> The amount of points in the set of points is based on the scale
'''

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def vlen(self):
        self.dist = (self.x**2+self.y**2)**(1/2)
        return self.dist



class grid:
    SCALE = 10
    #Grid is initialised using 2 vectors
    def __init__(self,base1,base2):
        self.v = base1
        self.u = base2
        self.dv = self.v.vlen()
        self.du = self.u.vlen()
    #To generate scale points 
    def generate_grid(self,scale):
        self.Points = []
        for i in range(1,scale):
            #self.Points.append( )
            pass
    def drawgrid(window):
        pass
    def animate_draw(window,rate):
        pass


