'''
Creating a grid class to represent the grid
> A grid is an abstraction of the vector space
> The standard basic grid is formed by the basis vectors i(0,1) and j(1,0)
> With the basis vectors, we can form a grid which is represented as a set of points in the memory
> The amount of points in the set of points is based on the scale
'''
from Matrix import *
import matplotlib.pyplot as plt

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def vlen(self):
        self.dist = (self.x**2+self.y**2)**(1/2)
        return self.dist



class grid:
    std_grid_list = [[0,0],[0,1],[1,0],[0,-1],[-1,0]]
    SCALE = 4
    #Grid is initialised using 2 vectors
    def __init__(self,base1,base2):
        self.v = base1
        self.u = base2
        self.dv = self.v.vlen()
        self.du = self.u.vlen()
    #To generate scale points 
    def generate_grid(self,scale = SCALE):
        self.gpoints = []
        #tr = np.array([[self.v.x,self.v.y],[self.u.x,self.u.y]])
        for k in range(1,scale):
            for el in self.std_grid_list:
                if el not in self.gpoints:
                    self.gpoints.append(el*k)
                    print(el*k)
            for i in range(len(self.gpoints)) :
                for j in range(i+1,len(self.gpoints)):
                    sum = [self.gpoints[i][0] + self.gpoints[j][0],self.gpoints[i][1] + self.gpoints[j][1]]
                    if sum not in self.gpoints:
                        self.gpoints.append(sum)
                        print(sum)
        return self.gpoints
    
    def drawgrid(window):
        pass
    def animate_draw(window,rate):
        pass

def main():
    print("JII")
    v1 = vector(1,2)
    v2 = vector(3,4)
    G = grid(v1,v2)
    pts = G.generate_grid()

    for i in pts:
        print(i,sep = "\t")
        plt.scatter(i[0],i[1])
    plt.show()
main()