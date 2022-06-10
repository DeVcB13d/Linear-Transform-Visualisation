
class Matrix:
    #constructor to intialize two matrices
    def __init__(self,mat1,mat2):
        self.A=mat1
        self.B=mat2
    def matrix_mul(self):
        #resultant vector in form of 2x1
        result = [[0],[0]]
        # iterate through rows of A
        for i in range(len(self.A)):
            # iterate through columns of B
            for j in range(len(self.B[0])):
                # iterate through rows of B
                for k in range(len(self.B)):
                    result[i][j] +=self.A[i][k] *self.B[k][j]
        for r in result:
            print(r)
            
    def determinant():
        pass
        

'''
class Vector:
    SCALE = 1
    def __init__(self,M):
        self.M = M
        self.rows = len(M)
        self.cols = len(M[0])
    def linear_transform(self):
        pass



class Grid:
    def __init__(self,points):
        self.points = points
    def draw_grid(self):
        #pygame program to draw based on points
        pass

def main():
    ar1 = [[1,3],[2,4]]
    ar2 = [[2],[4]]
    A1=Matrix(ar1,ar2)
    A1.matrix_mul()
   
main()
'''
