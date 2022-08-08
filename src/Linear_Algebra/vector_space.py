"""class Matrix:
    # Constructor to intialize two matrices
    def __init__(self,mat1):
        self.M = mat1
    # overloading the multiplication operator
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
            return result"""
def linearspace(basis_n):
    coordinates = []
    xi, yi = 0, 0
    #xj,yj  =1,0

    width=height=basis_n
    while xi < width:
      while yi < height:
        coordinates.append((xi, yi))
        yi += 1
        xi+= 1
    print(coordinates)
        
basi=20
linearspace(basi)    

"""for i in range(0,20):
            for j in range(0,20):
                b=c=set()
                b.add(basis[i][j]+1)
                i=i+1
                j=j+1
                return b"""