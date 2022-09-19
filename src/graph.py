# Module having the Coordinate Plane tools

import pygame as pg
import sys
from constants import *
from line import line
from linear_transform import linear_transform
import numpy as np
from approx import approx
pg.init()
screen = pg.display.set_mode((WIN_LEN,WIN_WID))
class Coordinate_plane:
    def __init__(self,screen,scale = MATH_SCALE,win_len = WIN_LEN,win_wid = WIN_WID,grid_size = WIN_LEN/20,depth_x = 10,depth_y = 10):
        '''
        Scale = size of 1 pixel in cm
        >>> scale = 40 for 800 X 800 means 40 pix = 1 cm
        >>> depth_x and depth_y shows the range of values shown in the screen
        '''
        self.scale = scale # 1cm = scale pixels
        self.depth_x = win_len//scale
        self.depth_y = win_wid//scale
        #self.scale = win_len / (2 * self.depth_x) #40
        self.screen = screen
        self.win_len = win_len
        self.win_wid = win_wid
        self.grid_size = grid_size
        self.draw_grid()
        self.draw_axis()
        self.insert_axis_text()
        self.state = [[1,0],[0,1]]
    def config_plane(self,plane_color = BLACK):
        self.screen.fill((plane_color))

    def coordinate(self,inx:float,iny:float)->tuple:
        """
        To input the coordinates and return its pygame UI equialent values
        1. Convert cartesian to pixels
        2. Shift of origin - (x,y) -> (x+win_len/2,y+win_wid/2)
        """
        # Pixel to cartesian conversion : (1,3) -> (10,30) -> (210,)
        pix_inx = inx * self.scale + self.win_len/2
        pix_iny = -1 * iny * self.scale + self.win_wid/2
        return (tuple([pix_inx,pix_iny]))
    def rev_coordinate(self,inx:float,iny:float)->tuple:
        '''
        To return the cartesian values from pygame UI values
        1. Shift origin back
        2. Convert pixels to cartesian

        TODO : Add approximations
        '''
        out_x= (inx - self.win_len/2)/(self.scale)
        out_y = (iny - self.win_wid/2)/(-1*self.scale)
        return (tuple([out_x,out_y]))
        
    def draw_grid(self,line_t = 1):
        '''
        To draw the main grid with each line spaced by gridsize

        NOTE: These markings are done directly based on pygame coordinate system and not on the cartesian one
        '''
        # Drawing vertical lines
        vert_ini_pos = [0, 0]
        vert_fin_pos = [0, self.win_wid]
        hor_ini_pos = [0, 0]
        hor_fin_pos = [self.win_len, 0]
        for i in range(1, self.win_len // self.depth_x + 2):
            pg.draw.line(self.screen, LAV, vert_ini_pos, vert_fin_pos,line_t)
            vert_ini_pos[0] += self.scale
            vert_fin_pos[0] += self.scale
        for i in range(1, self.win_wid // self.depth_y + 2):
            pg.draw.line(self.screen, LAV, hor_ini_pos, hor_fin_pos,line_t)
            hor_ini_pos[1] += self.scale
            hor_fin_pos[1] += self.scale
    def draw_axis(self,axis_color = YELLOW,axis_thickness = 3):
        """
        To draw the coordinate axes
        """
        posX =self.win_len/2
        pg.draw.line(self.screen,axis_color,(posX,0),(posX,self.win_wid),axis_thickness)
        posY = self.win_wid/2
        pg.draw.line(self.screen,axis_color,(0, posY),(self.win_len, posY),axis_thickness)
    def draw_line(self,point1,point2,thickness,color ):
        # To draw a a line given 2 coordinates onto the screen
        # Creating a line object
        to_draw_line = line(point1[0],point2[0],point1[1],point2[1])
        #print("slope : ",to_draw_line.slope)
        #print("y intercept : ",to_draw_line.y_inter)
        # top_x = x for y = 10         
        top_y = self.depth_y
        top_x = to_draw_line.get_x(top_y) 
        top = self.coordinate(top_x,top_y)
        end_y = -1*self.depth_y
        end_x = to_draw_line.get_x(end_y)
        #print("top_x : ",top_x,"top_y",top_y)
        #print("end_x : ",end_x,"end_y",end_y)
        end = self.coordinate(end_x,end_y)
        pg.draw.line(self.screen,color,top,end,thickness)
        #print(top,end)
        #print("DONE")
    def transform(self,base1,base2,color = PINK):
        '''
        Draw transformation onto the plane given 2 vectors base1 and base2
        Steps : 
        1. Create a linear transform object with the bases as matrix
        2. for Each element in x_trans_lines and y_trans lines plot the line

        TODO : Check for extremum points
        '''
        trans_matrix = (np.array([base1,base2]))
        #trans_matrix = np.transpose(trans_matrix)
        Linear = linear_transform(trans_matrix)
        # Drawing multiple lines
        #print("x transform lines : \n")
        #print(Linear.x_trans_lines)
        self.draw_vector((0,0),tuple([base1[0],base2[0]]),RED,5)
        self.draw_vector((0,0),tuple([base1[1],base2[1]]),GREEN,5)
        for Tline in Linear.x_trans_lines:
            #print("Tline : ",Tline)
            self.draw_line(tuple([Tline[0][0],Tline[1][0]]),tuple([Tline[0][1],Tline[1][1]]),2,color)
        #print(Linear.y_trans_lines)
        for Tline in Linear.y_trans_lines:
            #print("Tline : ",Tline)
            self.draw_line(tuple([Tline[0][0],Tline[1][0]]),tuple([Tline[0][1],Tline[1][1]]),2,color)
        self.draw_vector((0,0),tuple([base1[0],base2[0]]),RED,3)
        self.draw_vector((0,0),tuple([base1[1],base2[1]]),GREEN,3)
        self.state = trans_matrix
    def clear_screen(self):
        self.screen.fill(BLACK)
        self.draw_axis()
        self.draw_grid()
        self.insert_axis_text()
        self.state = [[1,0],[0,1]]
    def draw_vector(self,ini_pos,fin_pos,color = PINK,thickness = 4):
        ini_pos_pg = self.coordinate(ini_pos[0],ini_pos[1])
        fin_pos_pg = self.coordinate(fin_pos[0],fin_pos[1])
        pg.draw.line(self.screen,color,ini_pos_pg,fin_pos_pg,thickness)
    def insert_axis_text(self):
        font = pg.font.Font('freesansbold.ttf', 15)
        for i in range(-self.depth_x,self.depth_x):
            txt = str(i)
            text1 = font.render(txt, True,YELLOW)
            position_x = list(self.coordinate(0,i))
            position_x[0]+=20
            position_x=tuple(position_x)
            textRect = text1.get_rect()
            textRect.center = ((position_x))
            self.screen.blit(text1,textRect)
        for j in range(-self.depth_y,self.depth_y):
            txt = str(j)
            text = font.render(txt,True,YELLOW)
            position_y = list(self.coordinate(j,0))
            position_y[1]+=20
            position_y = tuple(position_y)
            textRect = text.get_rect()
            textRect.center = ((position_y))
            self.screen.blit(text,textRect)
    def change_scale(self,new_scale):
        self.scale  = new_scale
        self.depth_x = self.win_len//self.scale
        self.depth_y = self.win_wid//self.scale
        self.clear_screen()
        self.draw_grid()
        self.draw_axis()
        self.insert_axis_text()
        # To retain the transform 
        print(self.state)
        if (self.state != BASIS):
            print("HII")
            self.transform(self.state[0],self.state[1])
    def put_onto_screen(self,txt,position,size = 20,color = RED,bgcolor = LIGHT_BLUE):
        font = pg.font.Font('freesansbold.ttf', size)
        text1 = font.render(txt,True,color,bgcolor)
        position_x = list(self.coordinate(position[0],position[1]))
        position_x=tuple(position_x)
        textRect = text1.get_rect()
        textRect.center = ((position_x))
        self.screen.blit(text1,textRect)
    def eigen_vectors(self,trans_matrix : np.array):
        # To highlight the eigenvectors in a given transformation
        self.clear_screen()
        pg.display.update()
        pg.time.wait(100)
        values,vectors = np.linalg.eig(trans_matrix)
        self.draw_line((0,0),tuple(vectors[0]),4,LIME)
        self.disp_vector(vectors[0])
        self.draw_line((0,0),tuple(vectors[1]),4,LIME)
        self.disp_vector(vectors[1])
        print("Transformed Plane : ")
        x = input("")
        self.transform(trans_matrix[0],trans_matrix[1])
        #self.transform(tuple(vectors[0]),tuple(vectors[1]),RED)
    def eigen_vectors_2(self,trans_matrix : np.array):
        values,vectors = np.linalg.eig(trans_matrix)
        self.draw_vector((0,0),tuple(vectors[0]),ORANGE)
        self.put_onto_screen("Original_1",tuple(vectors[0]))
        self.draw_vector((0,0),tuple(vectors[1]),ORANGE)
        self.put_onto_screen("Original_2",tuple(vectors[1]))
        pg.display.update()
        pg.display.flip()
        pg.time.wait(4000)
        self.clear_screen()
        self.draw_vector((0,0),tuple(vectors[0]),ORANGE)
        self.draw_vector((0,0),tuple(vectors[1]),ORANGE)
        self.transform(trans_matrix[0],trans_matrix[1])
        pg.display.update()
        pg.display.flip()
        pg.time.wait(4000)
    
        self.draw_line((0,0),tuple(vectors[0]),4,LIME)
        self.disp_vector(vectors[0])
        self.draw_line((0,0),tuple(vectors[1]),4,LIME)
        self.disp_vector(vectors[1])


    def solve(self,A : np.array,b : np.array):
        # To solve a linear equ
        self.clear_screen();
        Ainv = np.linalg.inv(A)
        res = np.matmul(b,Ainv)
        self.disp_vector(b,LAV,15)
        self.draw_vector((0,0),tuple(b),ORANGE,5)
        pg.time.wait(4000)
        pg.display.flip()
        self.transform(A[0],A[1],LIME)
        pg.time.wait(4000)
        pg.display.flip()
        self.draw_vector((0,0),tuple(res),ORANGE,5)
        self.disp_vector(res,LAV,15)
    def disp_vector(self,vector,color = LIGHT_BLUE,size = 10):
        font = pg.font.Font('freesansbold.ttf', size)
        txt = str(tuple([round(vector[0],2),round(vector[1],2)]))
        text1 = font.render(txt,True,color)
        position_x = list(self.coordinate(vector[0],vector[1]))
        position_x=tuple(position_x)
        textRect = text1.get_rect()
        textRect.center = ((position_x))
        self.screen.blit(text1,textRect)
    def multiply(self,p1,p2):
        self.transform(p1[0],p1[1])
        pg.display.update()
        pg.display.flip()
        print("Generated transform of matrix 1")
        self.put_onto_screen(" ",(0,0))
        pg.display.update()
        pg.display.flip()
        pg.time.wait(3000)
        p1_n = np.array(p1)
        p2_n = np.array(p2)
        p3 = np.matmul(p1_n,p2_n)
        self.clear_screen()
        print("Generated transform of matrix 2")
        self.transform(p3[0],p3[1])






def run():
    pg.display.set_caption('Linear transformation')
    screen.fill(BLACK)
    pg_icon = pg.image.load('media\logo.jpg')
    pg.display.set_icon(pg_icon)
    run = True
    Plane = Coordinate_plane(screen)
    print("Welcome to the Linear Transforms visualization interface : ")
    print("Here are the currently available functionalities")
    print("A. Linear Transforms")
    print("B. Matrix Multiplication")
    print("C. Change_scale")
    print("D. Draw eigenvectors")
    print("E. Clear the screen")
    print("F. Linear Equation")
    while run:
        pg.time.wait(60)
        keys = pg.key.get_pressed()
        if (keys[pg.K_a]):
            Plane.clear_screen()
            p1 = eval(input("Enter Transform Matrix : "))
            Plane.transform(p1[0],p1[1])
        elif (keys[pg.K_b]):
            Plane.clear_screen()
            p1 = eval(input("Enter Matrix 1 : "))
            p2 = eval(input("Enter Matrix 2 : "))
            Plane.multiply(p1,p2)
        elif(keys[pg.K_c]):
            c = int(input("Enter the new scale : "))
            Plane.change_scale(c)
        elif(keys[pg.K_d]):
            p1 = eval(input("Enter Transform Matrix : "))
            Plane.eigen_vectors_2(p1)
        elif(keys[pg.K_e]):
            Plane.clear_screen()
        elif(keys[pg.K_f]):
            Plane.clear_screen
            A1 = np.array(eval(input("Enter Coefficient Matrix : ")))
            b1 = np.array(eval(input("Enter the constant matrix : ")))
            Plane.solve(A1,b1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                run = False
            if (event.type == pg.MOUSEBUTTONUP):
                # To print the selected coordinate
                pos = pg.mouse.get_pos()
                #Plane.clear_screen()
                a,b = Plane.rev_coordinate(pos[0],pos[1])
                print(approx(a),approx(b))
            pg.display.update()
        pg.display.update()   


while True:
    run()


