import numpy as np
from numpy.linalg import eig
import random
import numpy as np

class matrix:
    def __init__(self,mat):
        self.M=mat
    def detMatrix(self,M):
        if(len(self.M) != len(self.M[0])):
            error = "Matrix is not square"
            return error
        else:
            order = len(self.M)
            det = (self.M[0][0]*self.M[1][1]) - (self.M[0][1]*self.M[1][0])
            return det
    def transposeMatrix(self,M):
        transpose = [[0 for a in range(0, len(self.M))] for b in range(0, len(self.M[0]))]
        for i in range(0, len(self.M)):
           for j in range(0, len(self.M[0])):
            transpose[j][i] = self.M[i][j]
        return transpose
    def showMatrix(self,M):
        for i in range(0, len(self.M)):
            for j in range(0, len(self.M[0])):
                print(self.M[i][j], end = ' ')

            print('\n')
    def eigen(self,M):
<<<<<<< HEAD
        #k=0
        for k in range(0,100):
=======
        mat1=np.M
        print(mat1)
        Val,Vec=eig(mat1)
        print("Eigen values of the given matrix:")
        print(Val)
        print("Eigen vectors of the given matrix:")
        print(Val)


        """for k in range(0,100):
>>>>>>> 0e0bee516a24b882c8cb034a533c52f18eb199a5
            #k=random.randint(1,100)
            I=[[k,0],[0,k]]
            A=[self.M-I]
            b=self.detMatrix(A)
            if b==0:
                print("Eigen values:")
                print(k)"""

def run():
        print("Matrix format: ")
        mat = [[1,4],[8,9]]
        #print(mat)
        M=matrix(mat)
        mat1=M.detMatrix(mat)
        M1=matrix(mat)
        mat2=M1.transposeMatrix(mat)
        print(mat2)
        #M1.eigen(mat)
run()


