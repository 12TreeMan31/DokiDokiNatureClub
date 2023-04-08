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
joinclub = pygame.image.load("/home/anna/0_Code/assets/bg_joinclub.png")
taiko= pygame.image.load("/home/anna/0_Code/assets/bg_taiko.png")
textbox = pygame.image.load("/home/anna/0_Code/assets/textbox.png")



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
left=(-150,40)
mid=(350,40)
right=(800,40) 

scene=[["Me", clubfair, none,none,none,"(It's my third week at the Amazon Academy of Brazil)", "(My teachers have been telling me to join a club)", "(But I'm not really interested in anything...)"], 
       ["Me", joinclub, none,none,none,"(...huh...What's this)","(The Nature Club?)"],
        ["Poster", joinclub, none, none, none, " [This is the Nature club, come save the Planet with us!!!]"],
        ["Me", joinclub , none, none, none, "(Sure, Why not...)" ],
        ["Janice", nature ,  mid, left, right, "Welcome to the Nature club!!!!", "We're so happy you're here!", "So to the start the year off, we'll do an activity!", "This years theme is saving the rainforest." ],
        ["Maddie", nature, mid, left, right, "How about we let the new member decide?"],

       ["Olivia", nature , mid, none, none, "Hey new guy, glad to hear you want to help me plant trees!", "Its really important that we work to replant the rainforst"," Did you know...", " more than 200,000 acres of rainforest is destroyed each day.", "But with enough people committed to the cause, we can save the rainforests!" ],
        ["Olivia", taiko, mid, none, none, "To plant trees, click F or J when the tree aligns with the yellow circle!", "Easy enough right?", "Ready? Begin!"],
        ##cue taiko
        
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
        message=scene[scenenum][0]+": "+scene[scenenum][i]
        print(message)
        pygame.draw.rect(screen, (0, 0, 0), (1280/2-550-5,15-5,1110,120))
        pygame.draw.rect(screen, (192, 179, 199), (1280/2-550,15,1100,110))
        text= font.render(message, True, (0,0,0))
        screen.blit(text, (1280/2-525, 35) )
        
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
