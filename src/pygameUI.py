import pygame, sys

# CONSTANTS
BLUE = (0, 0, 51)
YELLOW = (255, 255, 0)
LAV = (229, 204, 255)
wind_len = 500
wind_brea = 500
grid_line_width = 3
pygame.init()
# SCREEN
screen = pygame.display.set_mode((wind_len, wind_brea))
pygame.display.set_caption('Linear transformation')
screen.fill(BLUE)
pygame_icon = pygame.image.load('media\logo.jpg')
pygame.display.set_icon(pygame_icon)

def draw_main_grid(gridsize):
    posX =wind_brea//2
    pygame.draw.line(screen, YELLOW, (posX,0), (posX,wind_len), 6)
    posY = wind_len//2
    pygame.draw.line(screen, YELLOW, (0, posY), (wind_brea, posY), 6)
    # Drawing vertical lines
    vert_ini_pos = [0, 0]
    vert_fin_pos = [0, wind_len]
    hor_ini_pos = [0, 0]
    hor_fin_pos = [wind_brea, 0]
    for i in range(1, wind_len // 10 + 2):
        pygame.draw.line(screen, LAV, vert_ini_pos, vert_fin_pos, grid_line_width)
        vert_ini_pos[0] += gridsize
        vert_fin_pos[0] += gridsize
    for i in range(1, wind_brea // 10 + 2):
        pygame.draw.line(screen, LAV, hor_ini_pos, hor_fin_pos, grid_line_width)
        hor_ini_pos[1] += gridsize
        hor_fin_pos[1] += gridsize
def draw_line():
    posX =wind_brea//2
    pygame.draw.line(screen, YELLOW, (posX,0), (posX,wind_len), 2)
    posY = wind_len//2
    pygame.draw.line(screen, YELLOW, (0, posY), (wind_brea, posY), 2)


def main():
    run = True
    draw_main_grid(31)
    #draw_line()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                run = False
        pygame.display.update()


main()
