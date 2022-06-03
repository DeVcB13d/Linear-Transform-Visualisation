from unittest import result


class Matrix:
    def __init__(self,mat):
        self.M=mat
    def matrix_mul(self,A,span):
        result = span.M
        for i in range(len(A.M)):
            for j in range(len(span.M)):
                result[i][j]=0
                for k in range(len(span)):
                    result[i][j]+=A[i][k]*span[k][j]
        return result
    def determinant():
        pass
        


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
'''

def main():
    ar1 = [[1,3],[2,4]]
    ar2 = [2,4]
    A1 = Matrix(ar1)
    A2 = Matrix(ar2)
    res = A1.matrix_mul(A1,A2)
    print(res)
    print(ar1*ar2)


main()