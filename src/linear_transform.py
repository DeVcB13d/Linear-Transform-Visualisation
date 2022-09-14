'''
class to perform linear transformation


input : transform matrix

1. Generating axes lines as matrices
    *Eg :[[0,0],[1,0]] is y axis
        [[0,0],[1,0]] is x axis
    * The axes matrices would be of the form : 
    * [[0,0],[1,0]] , [[0,1],[1,1]] , ..... , [[0,10],[1,10]] - x_axis_lines
    * [[0,-1],[1,-1]] , .... , [[0,-10],[1,-10]] 
    * [[0,0],[0,1]] , [[1,0],[1,1]] , ..... , [[10,0],[10,1]] - y_axis_lines
    * [[-1,0],[-1,1]] , [[-2,0],[-2,1]] , ..... , [[-10,0],[-10,1]] 

2. After these axes are generated, they need to be transformed :
    > x_trans_lines = trans_mat * x_axis_lines
    > y_trans_lines = trans_mat * y_axis lines

3. Plotting the transformed matrices onto screen :
    > Modify the line class to be able to plot solely based on an input matrix
'''
import numpy as np

class linear_transform:
    def __init__(self,trans_mat):
        self.M = np.array(trans_mat)
        self.x_axis_lines,self.y_axis_lines = self.generate_axis_lines()
        self.x_trans_lines,self.y_trans_lines = self.apply_transform()
    def generate_axis_lines(self,limit = 100,basis = [[1,0],[0,1]]):
        x_axis_lines = []
        x_base_matrix = np.array([[0,0],basis[1]])
        T = np.array(x_base_matrix.copy())
        x_axis_lines.append(T)
        #x_base_matrix[1][0] = 1
        #print(x_axis_lines)
        #print("base mat : ",x_base_matrix)
        for i in range(1,limit):
            temp = x_base_matrix.copy()
            temp[0][0] = i
            temp[0][1] = i
            #print("temp1 " , temp)
            x_axis_lines.append(temp.copy())
            temp[0][0] = -1*i
            temp[0][1] = -1*i
            x_axis_lines.append(temp.copy())
            #print("x axis lines ",i,":",x_axis_lines)
        y_axis_lines = []
        y_base_matrix = np.array([basis[1],[0,0]])
        T2 = np.array(y_base_matrix.copy())
        y_axis_lines.append(T2)
        for i in range(1,limit):
            temp = y_base_matrix.copy()
            temp[1][0] = i
            temp[1][1] = i
            y_axis_lines.append(temp.copy())
            temp[1][0] = -1*i
            temp[1][1] = -1*i
            y_axis_lines.append(temp.copy())   
        return x_axis_lines,y_axis_lines
    def apply_transform(self):
        x_trans_lines = []
        y_trans_lines = []
        for xline in self.x_axis_lines:
            x_trans_lines.append(np.matmul(self.M ,xline))
            #y_trans_lines.append(self.M * yline)
        for yline in self.y_axis_lines:
            y_trans_lines.append(np.matmul(self.M,yline))
        return x_trans_lines,y_trans_lines




def main():
    X = linear_transform([[0,1],[1,1]])
    print(X.x_axis_lines)
    print(X.y_axis_lines)
    print(X.x_trans_lines)
    print(X.y_trans_lines)

#main()



