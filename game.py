import pygame
import sys

pygame.init()
font = pygame.font.SysFont("georgia", 50)

# create game window 

fps= 15
fpsClock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT= 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")


TEXT_COL = (255, 255, 255)

def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x, y))


objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }


        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def buttonPressed():
    print('Start Pressed')
    screen.fill((255, 209, 220))
    objects.clear()
    print(objects)
    screen.fill((255, 209, 220))


    











def quitPressed():
    print('Quit Pressed')
    pygame.QUIT()

Button(30, 200, 400, 100, 'start', buttonPressed)
Button(30, 400, 400, 100, 'quit', quitPressed)



screen.fill((255, 209, 220))
title= "Doki Doki Nature Club"
menutrue= True

runmenu = True 



    












while runmenu:
    screen.fill((255, 209, 220))
    drawText(title, pygame.font.SysFont("georgia", 70), TEXT_COL, 20 , 60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("hahaha")
        
        if event.type == pygame.QUIT:
            run = False
            pygame.display.update()

    for object in objects:
        object.process()

    pygame.display.flip()

        

    fpsClock.tick(fps)


game1= True
while game1:
    screen.fill((255, 209, 220))
    drawText(title, pygame.font.SysFont("georgia", 70), TEXT_COL, 20 , 60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("hahaha")
        
        if event.type == pygame.QUIT:
            run = False
            pygame.display.update()

    for object in objects:
        object.process()

    pygame.display.flip()

        

    fpsClock.tick(fps)




pygame.quit()


