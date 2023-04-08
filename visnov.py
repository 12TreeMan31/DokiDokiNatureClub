import pygame
from pygame.locals import *



# 2 - Initialize the game
pygame.init()

font= pygame.font.Font('freesansbold.ttf', 25)
width, height = 1280, 720
screen=pygame.display.set_mode((width, height))



imagesize=(700,700)

# Load images
clubfair= pygame.image.load("/home/anna/0_Code/assets/bg_clubfair.png")
nature= pygame.image.load("/home/anna/0_Code/assets/bg_natureclub.png")
dance = pygame.image.load("/home/anna/0_Code/assets/bg_dance.png")

happyotter= pygame.image.load("/home/anna/0_Code/assets/otter_happy.png")
sadotter= pygame.image.load("/home/anna/0_Code/assets/otter_sad.png")
happymorb= pygame.image.load("/home/anna/0_Code/assets/morpho_happy.png")
sadmorb= pygame.image.load("/home/anna/0_Code/assets/morpho_sad.png")
happyjag= pygame.image.load("/home/anna/0_Code/assets/jaguar_happy.png")
sadjag= pygame.image.load("/home/anna/0_Code/assets/jaguar_sad.png")

happyotter = pygame.transform.scale(happyotter, (imagesize))
sadotter = pygame.transform.scale(sadotter, (imagesize))
happymorb= pygame.transform.scale(happymorb, (imagesize))
sadmorb= pygame.transform.scale(sadmorb, (imagesize))
happyjag= pygame.transform.scale(happyjag, (imagesize))
sadjag= pygame.transform.scale(sadjag, (imagesize))

#







none=(-1000,-1000)
left=(-150,20)
mid=(350,20)
right=(800,20)

scene=[["Me", nature, none,none,none,"It's my third week at the Amazon Academy of Brazil", "My teachers have been hounding me about joining a club"], 
       ["Me", nature, none,none,none,"Hmmm... What's this?", "...", "Nature Club?"," Sure, Why not." ],
       
       
       
       
       
       
       
       
       
       
       
       
       ]
#[talker, bg, otterloc, morbloc,jagloc,messages...]

scenenum=-1

def scenebuild():
    i=5
    screen.fill(0)
    bg=scene[scenenum][1]
    screen.blit(bg,(0,0))
    
    screen.blit(happyotter,scene[scenenum][2] )
    screen.blit(happymorb,scene[scenenum][3] )
    screen.blit(happyjag,scene[scenenum][4])



    
    
    print(scene[scenenum])
    while i<= (len(scene[scenenum])-1):
        print(i)
        message=scene[scenenum][i]
        print(message)
        pygame.draw.rect(screen, (0, 0, 0), (1280/2-450-5,570-5,910,140))
        pygame.draw.rect(screen, (192, 179, 199), (1280/2-450,570,900,130))
        text= font.render(message, True, (0,0,0))
        screen.blit(text, (1280/2-400, 600) )
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i+=1

            if event.type==pygame.QUIT:
            # if it is quit the game
                pygame.quit() 
                exit(0)
        
    
    





# 4 - keep looping through
while scenenum<= len(scene):
    scenenum+=1
    scenebuild()

    
        
        
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scene+=1
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
