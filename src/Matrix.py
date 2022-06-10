
class Matrix:
    #constructor to intialize two matrices
    def __init__(self,mat1):
        self.M=mat1
    def __mul__(self,B):
        try:
            len(self.M[0]) == len(B.M)
        except:
            return "Error : Length cannot be multiplied"
        else:
            self.B = B
            #resultant vector in form of 2x1
            result_dim = (len(self.M[0]),len(B.M))
            result = [[0 for _ in range(result_dim[0])] for __ in range(result_dim[1])]
            # iterate through rows of M
            for i in range(len(self.M)):
                # iterate through columns of B
                for j in range(len(self.B.M[0])):
                    # iterate through rows of B
                    for k in range(len(self.B.M)):
                        result[i][j] +=self.M[i][k] *self.B.M[k][j]
            return result
    def __add__():
        pass
            
    def determinant():
        pass
        

def main():
    ar1 = [[1,3],[2,4]]
    ar2 = [[2],[4]]
    A1=Matrix(ar1)
    A2 = Matrix(ar2)
    res = Matrix(A1*A2)
    print(res.M)
   
if __name__ == "__main__": 
    main()
