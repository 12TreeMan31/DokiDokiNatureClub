import pygame
import sys


pygame.init()

# create game window 

fps= 60
fpsClock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT= 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")


TEXT_COL = (255, 255, 255)

def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x, y))

run = True 
while run:
    
    screen.fill((255, 209, 220))

    drawText("Doki Doki Nature Club!!", pygame.font.SysFont("georgia", 70), TEXT_COL, 20 , 60)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("hahaha")
        
        if event.type == pygame.QUIT:
            run = False
        
        pygame.display.update()
pygame.quit()