import pygame
import pygame_menu
import time, random
import sys




pygame.init()
window = pygame.display.set_mode((1280,720))

pink = pygame_menu.themes.THEME_BLUE.copy()
pink.title_background_color=(245, 103, 176)
pink.title_font = pygame_menu.font.FONT_NEVIS




def start():
    pass
    #PUT VISNOW.PY HERE!!!!
    import pygame








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



    happyotter= pygame.image.load("/home/anna/0_Code/assets/otter_happy.png")
    happymorb= pygame.image.load("/home/anna/0_Code/assets/morpho_happy.png")
    happyjag= pygame.image.load("/home/anna/0_Code/assets/jaguar_happy.png")

    happyotter = pygame.transform.scale(happyotter, (imagesize))
    happymorb= pygame.transform.scale(happymorb, (imagesize))
    happyjag= pygame.transform.scale(happyjag, (imagesize))

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
            
            #after taiko
            ["Olivia", nature, mid, left, right, "Great job!!!", "Thanks for helping me out!", "Because of you, the world is a better place!"],
            ["Janice", nature, mid, left, right, "Hey! How about we make a school dance to fundraise for...","...hmm..."],
            ["Maddie", nature, mid, left, right, "Oh I know!", "The Word WildLife Fund!"],
            ["Janice", nature, mid, left, right, "That sounds great!!", "Let's Dance!", "I'll get the preparations ready!"],
            ["Me", nature, mid, left, right, "Let's rock!"],
            ["", dance, none, none, none, "...A Few Days Later..."],
            ["Me", dance, none, none, none, "(I'll go join everyone else at the dance)", "(Looks like this is a game where I have to hit W, A, S, D in correlation to the arrows. )", "Am I ready?"],

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
        if scenenum==8:
            screenWidth=1280
            
            print("taikotime")
            clock = pygame.time.Clock()
            running = True
            global points
            points = 0
            good=pygame.image.load("good.png")
            ball = pygame.image.load("tree.png")
            bg = pygame.image.load("bg_taiko.png")
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
                    if self.points > 2:
                        running=False



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

            scene+=1


    
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
    
menu = pygame_menu.Menu('Doki Doki Nature Club', 1280, 720, theme=pink)
menu.add.button("Play", start)
menu.add.button("Quit", pygame_menu.events.EXIT)

menu.mainloop(window)
