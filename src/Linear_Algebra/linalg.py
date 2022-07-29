'''
Defining a matrix class to perform fundamental matrix operations
'''

class Matrix:
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
            return result
    def __add__(self,B):
        '''
        Function to add two matrices 
        '''    
        pass
    def determinant():
        pass


class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def vlen(self):
        self.dist = (self.x**2+self.y**2)**(1/2)
        return self.dist

# Defining a vectorspace class

class vector_space:
    '''
    Initializing a vector space
    '''
    def __init__(self,bases):
        self.bases = bases
    def generate_space(self,points):
        
