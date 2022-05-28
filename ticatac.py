import pygame
import numpy as npy


#Constant values
WIN_LEN,WIN_WID = 600,800
FPS = 60
COR = 35
TILE_LEN = 155
BG_COLOUR = (160,160,160)
TILE_COLOUR = (96,96,96)
X_COLOUR = (153,255,255)
O_COLOUR = (255,255,102)
BLACK = (0,0,0)
#______________________________


#Initialiasing the mainscreen
pygame.init()
#Setting the display with length and breadth
screen = pygame.display.set_mode((WIN_LEN,WIN_WID))
pygame.display.set_caption("Tic Tac Toe")

#Declaring a 3X3 Matrix to represent game states
state = npy.zeros((3,3))

#Function to draw X or O on the screen
#based on the state matrix
def drawXO():
    font = pygame.font.Font('freesansbold.ttf', 90)
    for row in range(0,3):
        for col in range(0,3):
            if state[row][col] == 1:
                C = col+1 #To get correct positions on the screen
                R = row+1
                #Draws X onto the screen
                text = font.render('X', True,X_COLOUR,TILE_COLOUR)
                textRect = text.get_rect()
                #position to print x
                #x = col*corner + (2*col-1)(tile_len/2)
                textRect.center = (C*COR + (2*C - 1)*(TILE_LEN/2),R*COR + (2*R - 1)*(TILE_LEN/2))
                screen.blit(text, textRect)
                
            elif state[row][col] == 2:
                C = col+1
                R = row+1
                text = font.render('O', True,O_COLOUR,TILE_COLOUR)
                textRect = text.get_rect()
                textRect.center = (C*COR + (2*C - 1)*(TILE_LEN/2),R*COR + (2*R - 1)*(TILE_LEN/2))
                screen.blit(text, textRect)
#Function to set player mark on the state matrix
def mark(row,col,player):
    state[row][col] = player
#Function to return if the row is marked or not
def is_marked(row,col):
    return state[row][col] == 0
#Function to draw stuff onto the display
def set_display():
    screen.fill(BG_COLOUR)
    #To draw 9 tiles to mark X and O
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR,COR,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*2+TILE_LEN,COR,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*3+TILE_LEN*2,COR,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR,COR*2+TILE_LEN,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*2+TILE_LEN,COR*2+TILE_LEN,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*3+TILE_LEN*2,COR*2+TILE_LEN,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR,COR*3+TILE_LEN*2,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*2+TILE_LEN,COR*3+TILE_LEN*2,TILE_LEN,TILE_LEN))
    pygame.draw.rect(screen,TILE_COLOUR,pygame.Rect(COR*3+TILE_LEN*2,COR*3+TILE_LEN*2,TILE_LEN,TILE_LEN))
    #Draw a line below the tiles
    pygame.draw.line(screen,TILE_COLOUR,(0,600),(600,600),10)
    #Creating a reset button
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render('RESET', True,BG_COLOUR,TILE_COLOUR)
    textRect = text.get_rect()
    textRect.center = (300,750)
    screen.blit(text, textRect)

#Function to check if the player wins
def checkwin(player):
    ret = False
    for i in range(0,3): 
        for j in range(0,3):
            #Check rows for win
            if state[0][j]==state[1][j]==state[2][j]==player:
                ret = True
                break
            #Check columns for win
            elif state[i][0]==state[i][1]==state[i][2]==player:#Check Columns
                ret = True
                break
    #Check diagonals for win
    if state[1][1]==state[2][2]==state[0][0]==player:
        ret = True
    elif state[1][1]==state[2][0]==state[0][2]==player:
        ret = True
    return ret

#Function to check wheter the state matrix is full
def is_full():
    f = 0
    for i in state:
        for j in i:
            if j != 0 :
                f+=1
    #F will show marked tiles
    if f == 9:
        return True
    else :
        return False

#Function to display appropriate Win/Draw messages
def win_message(result):
    font = pygame.font.Font('freesansbold.ttf', 60)
    if result == 1:
        text = font.render('X WON', True,X_COLOUR,BG_COLOUR)
        textRect = text.get_rect()
        textRect.center = (300,650)
        screen.blit(text, textRect)
    elif result == 2:
        text = font.render('O WON', True,O_COLOUR,BG_COLOUR)
        textRect = text.get_rect()
        textRect.center = (300,650)
        screen.blit(text, textRect)
    elif result == 3:
        text = font.render('DRAW', True,(0,0,0),BG_COLOUR)
        textRect = text.get_rect()
        textRect.center = (300,650)
        screen.blit(text, textRect)

#Function to reset the game
def reset():
    #Changing state matrix values to 0
    for i in range(0,3):
        for j in range(0,3):
            state[i][j] = 0
    #Calling to remove all marks and switch
    #to the initial display
    set_display()

#main function
def main():
    player = 1  #player 1 and 2
    game = True #Control game run
    run = True  #Control window exit
    set_display() #Changes blank screen
    while run:
        for event in pygame.event.get():
            #To Quit and  close window
            if event.type == pygame.QUIT :
                run = False
            #When the mouse is pressed
            if event.type == pygame.MOUSEBUTTONUP :
                #returns mouse XY position
                pos = pygame.mouse.get_pos()
                #If position is reset button
                if pos[1] > 700:
                    reset()
                    game = True
                    player = 1
                #If game is in running mode
                if game:
                    #To get the row and column based on input
                    Col = int((pos[0])//(TILE_LEN+COR))
                    Row = int((pos[1])//(TILE_LEN+COR))
                    if Row >= 3:
                        Row = 2
                    if Col >= 3 :
                        Col = 2
                    #If the tile is clicked and
                    #The state matrix is not full
                    if Row <= 2 and Col <=2 and not is_full() and pos[1] < 600 :
                        #If it is not marked
                        if is_marked(Row,Col):
                            #Switching the players
                            if player == 1:
                                player = 2
                            elif player == 2:
                                player = 1
                            #Marking the statematrix
                            mark(Row,Col,player)
                            #Check for win and disabling further changes
                            if checkwin(player):
                                win_message(player)
                                game = False
                            #When game is a draw
                            elif is_full():
                                win_message(3)
                                game = False
            #Draws X and O based on state matrix after each mouseclick
            drawXO()
        #Update the display
        pygame.display.update()
    pygame.quit()


main()