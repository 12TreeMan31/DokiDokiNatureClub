# Example file showing a basic pygame "game loop"
import pygame, time, random
import sys

# pygame setup
pygame.init()
screenWidth = 1280
screenHight = 720

screen = pygame.display.set_mode((screenWidth, screenHight))
clock = pygame.time.Clock()
running = True
global points
points = 0

ball = pygame.image.load("assets/tree.png")
bg = pygame.image.load("assets/bg_taiko.png")
class redThing:
    def __init__(self, x):
        self.points = 0
        self.x = x - 50
        self.y = 100
    #Moves thing
    def move(self):
        self.x = self.x - 20
        screen.blit(ball, (self.x, self.y))
        if self.x < -1000:
            self.x = screenWidth + random.randint(0, 1000)
    #Hit detection
    def isHit(self):
        if self.x < 0:
            self.x = screenWidth + random.randint(0, 1000)
            self.points +=1
            screen.blit(good, (self.x, self.y))
            print(self.points)
        if self.points == 10:
            pygame.quit()



s = redThing(screenWidth)
d = redThing(screenWidth)



def usrInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Keyboard 
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "f": 
                print("f")
                s.isHit()
                d.isHit()
            if key == "j":
                print("j")
                s.isHit
                d.isHit()


TEXT_COL = (89, 78, 76)
font = pygame.font.SysFont("georgia", 50)

def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x, y))

while running:
    usrInput()

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(bg, (0, 0))
    drawText("Try to plant 20 trees", pygame.font.SysFont("georgia", 70), TEXT_COL, 20 , 60)
    s.move()
    d.move()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
