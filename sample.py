import pygame
from variables import *
SCREEN_HEIGHT = 600
BG_COLOUR = (160,160,160)
SCREEN_WIDTH = 600
pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
screen.fill(BG_COLOUR)
pygame.display.set_caption("Linear Tansforms")

def draw():
    #v1 = list(input("Enter 2 elements"))
    #v2 = list(input("Enter 2 elements"))
    pygame.draw.line(screen,(78,86,68),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),10)
    pygame.draw.line(screen,(64,57,55),(0,SCREEN_HEIGHT/2),(SCREEN_HEIGHT/2,SCREEN_WIDTH),10)
def main():
    draw()
    run = True
    pygame.display.update()
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
        pygame.display.update()
    pygame.quit()


main()

