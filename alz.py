import pygame
import sys
# https://www.soundjay.com/communication-sounds.html
# second track
# setting up window
pygame.init()
screen = pygame.display.set_mode((500,650))
pygame.display.set_caption("Alzhemier's")
clock = pygame.time.Clock()
doctor1 = True

# Fonts
font1 = pygame.font.SysFont("Monospace", 30)
font2 = pygame.font.SysFont("Monospace", 20)
font3 = pygame.font.SysFont("Monospace", 15)

# sets scene to 0.0
scene = 0.0

# words for opening page 56, 0, 113
title = font1.render("Alzheimer's", True, (0, 0, 0))
start = font2.render("click anywhere to continue", True, (0, 0, 0))

# instantiating names for dialogue, **colors are subject to change**
you = font2.render("You: ", True, (0, 0, 0))
david = font2.render("David: ", True, (0, 0, 0))
unknown = font2.render("???: ", True, (0, 0, 0))
kristyanne = font2.render("Kristy-Anne: ", True, (0, 0, 0))
doctor = font2.render("Dr. Pineapple: ", True, (0, 0, 0))
thought = font2.render(" ", True, (0, 0, 0))
jacob = font2.render("Jacob: ", True, (0, 0, 0))
ellen = font2.render("Ellen: ", True, (0, 0, 0))

# making yes and no buttons for act one scene 1
yesDoc = pygame.Rect(75, 550, 150, 80)
noDoc = pygame.Rect(275, 550, 150, 80)
yesTurn = pygame.Rect(100, 550, 130, 50)
noTurn = pygame.Rect(300, 550, 130, 50)
claire = pygame.Rect(100, 550, 130, 50)
catherine = pygame.Rect(300, 550, 130, 50)
neighbor = pygame.Rect(100, 550, 130, 50)
gf = pygame.Rect(300, 550, 130, 50)
yesStove = pygame.Rect(100, 550, 130, 50)
noStove = pygame.Rect(300, 550, 130, 50)
yesHelp = pygame.Rect(100, 550, 130, 50)
noHelp = pygame.Rect(300, 550, 130, 50)
yesGroc = pygame.Rect(75, 550, 150, 80)
noGroc = pygame.Rect(275, 550, 150, 80)
yesHelp1 = pygame.Rect(100, 550, 120, 70)
noHelp1 = pygame.Rect(300, 550, 120, 70)
yesCall= pygame.Rect(100, 550, 130, 50)
noCall = pygame.Rect(300, 550, 130, 50)

done = False

def dialogue(line, speaker):
    if scene < 2 and scene > 0:
        pygame.draw.rect(screen, (207, 214, 255), (0, 400, 500, 700), 0)
    elif scene > 1.9999 and scene < 3:
        pygame.draw.rect(screen, (164, 148, 255), (0, 400, 500, 700), 0)
    elif scene > 3 and scene < 3.35:
        pygame.draw.rect(screen, (112, 105, 255), (0, 400, 500, 700), 0)
    elif scene > 3.34:
        pygame.draw.rect(screen, (199, 167, 240), (0, 400, 500, 700), 0)
    screen.blit(speaker, (30, 420))
    pygame.display.update()
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.init()
    pygame.mixer.music.load("computer-keyboard-2.wav")
    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play(-1)
    x = 40
    y = 450
    i = 0
    for i in range (len(line)):
        if(x >= 400 and line[i-1] == " "):
            x = 40
            y += 30
        else:
            x += 10
        letter = font3.render(line[i], True, (0, 0, 0))
        screen.blit(letter, (x, y))
        pygame.display.flip()
        pygame.time.wait(30)
    pygame.mixer.music.stop()

def dialogueCredit(line):
    x = 40
    y = 170
    i = 0
    for i in range (len(line)):
        if(x >= 400 and line[i-1] == " "):
            x = 40
            y += 30
        else:
            x += 10
        letter = font3.render(line[i], True, (255, 255, 255))
        screen.blit(letter, (x, y))
        pygame.display.flip()
        pygame.time.wait(40)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    # continuosly updates position of the cursor
    mousePos = pygame.mouse.get_pos()
    # opening title screen
    if(scene == 0.0):
        opening = pygame.image.load('mmexport15657374020671.jpg')
        screen.blit(opening, (0,0))
        pygame.display.update()
        screen.blit(title, ((500 - title.get_width()) // 2, (600 - title.get_height()) // 2))
        screen.blit(start, ((500 - start.get_width()) // 2, (600 - start.get_height()) // 2 + 30))
        pygame.display.update()
        scene = 0.1
    # when the user clicks opening screen
    # act 1 opening screen appears
    if(scene == 0.1 and event.type == pygame.MOUSEBUTTONUP):
        screen.fill((0, 0, 0))
        act1 = font1.render("ACT ONE", True, (255, 255, 255))
        mid = font1.render("MID (2 YEARS)", True, (255, 255, 255))
        screen.blit(act1, ((500 - act1.get_width()) // 2, (600 - act1.get_height()) // 2))
        pygame.draw.line(screen, (255, 255, 255), (150, 320), (350, 320), 1)
        screen.blit(mid, ((500 - mid.get_width()) // 2, (600 - act1.get_height()) // 2 + 50))
        pygame.display.update()
        scene = 1.0

    # first scene of act one
    if(scene == 1.0 and event.type == pygame.MOUSEBUTTONDOWN):
        screen.fill((0, 0, 0))
        doctorQuesScene = pygame.image.load('scene 1.png')
        screen.blit(doctorQuesScene, (0,0))
        pygame.display.update()
        dialogue("Mom, let's go to the doctor to check up on your health. I've noticed your memory has been a little off lately......", david)

        # drawing yes and no buttons (box only)
        pygame.draw.rect(screen, [255, 255, 255], yesDoc)
        pygame.draw.rect(screen, [255, 255, 255], noDoc)

        # rendering and printing button text
        yes1 = font3.render("yes, i should", True, (199, 167, 255))
        yes2 = font3.render("probably get it", True, (199, 167, 255))
        yes3 = font3.render("checked :/", True, (199, 167, 255))
        screen.blit(yes1, (85, 560))
        screen.blit(yes2, (85, 580))
        screen.blit(yes3, (85, 600))
        no1 = font3.render("no, i'm not", True, (199, 167, 255))
        no2 = font3.render("going insane", True, (199, 167, 255))
        no3 = font3.render(">:(", True, (199, 167, 255))
        screen.blit(no1, (300, 560))
        screen.blit(no2, (295, 580))
        screen.blit(no3, (330, 600))
        pygame.display.update()
        scene= 1.001
    # what happens when the player chooses yes
    # diagnosis
    if scene == 1.01 and yesDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        threeMonths = font2.render("Three months later", True, (255, 255, 255))
        screen.blit(threeMonths, ((500 - threeMonths.get_width()) // 2, (600 - threeMonths.get_height()) // 2))
        pygame.display.update()
        scene = 1.001
    if scene == 1.001 and event.type == pygame.MOUSEBUTTONDOWN:
        doctorScene = pygame.image.load('scene 2.png')
        screen.blit(doctorScene, (0,0))
        pygame.display.update()
        dialogue("After analyzing all the tests, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.111
    # leaving doctor's office
    if scene == 1.111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Alright, thank you.", david)
        scene = 1.1111
    # car scene/going home
    if scene == 1.1111 and event.type == pygame.MOUSEBUTTONDOWN:
        carScene = pygame.image.load('scene 3.png')
        screen.blit(carScene, (0,0))
        pygame.display.update()
        dialogue("*did David miss a turn?*", you)
        pygame.draw.rect(screen, (255, 255, 255), yesTurn)
        pygame.draw.rect(screen, (255, 255, 255), noTurn)
        y = font2.render("yes", True, (199, 167, 255))
        n = font2.render("no", True, (199, 167, 255))
        screen.blit(y, (150, 560))
        screen.blit(n, (355, 560))
        pygame.display.update()
        scene = 1.111111
    # if user says there was a turn
    if scene == 1.111111 and yesTurn.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David, I think you missed a turn.", you)
        scene = 1.1111111
    # david's response to the comment
    if scene == 1.1111111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("No, mom, it's  the next turn.", david)
        scene = 1.11111111
    if scene == 1.11111111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, I'm sorry :(", you)
        scene = 1.2
    # if user says there wasn't a turn
    if scene == 1.111111 and noTurn.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David, how much longer until we're home?", you)
        scene = 1.1111111111
    if scene == 1.1111111111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("About 5 more minutes.", david)
        scene = 1.2

    # what happens when the player chooses no
    if scene == 1.01 and noDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok. Come on. Let's go on our daily walk.", david)
        scene = 1.2
        doctor1 = False

    # meeting Kristy-Anne scene
    if scene == 1.2 and event.type == pygame.MOUSEBUTTONDOWN:
        neighborScene = pygame.image.load('meeting ka_1.jpg')
        screen.blit(neighborScene, (0,0))
        pygame.display.update()
        dialogue("Oh hello! You must be my new neighbors. My name is Kristy-Anne. I just moved in next door.", unknown)
        scene = 1.21

    if scene == 1.21 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Hello! It’s nice to see a new face around here. You like a good woman to be in my David’s life.", you)
        scene = 1.22

    if scene == 1.22 and event.type == pygame.MOUSEBUTTONDOWN:
        davidBlush = pygame.image.load('blushing david_1.jpg')
        screen.blit(davidBlush, (0,0))
        pygame.display.update()
        dialogue("David’s face turns red and the girl giggles.", thought)
        scene = 1.23

    if scene == 1.23 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom! You must be tired. Let’s get you inside.", david)
        scene = 1.24

    if scene == 1.24 and event.type == pygame.MOUSEBUTTONDOWN:
        screen.blit(neighborScene, (0,0))
        pygame.display.update()
        dialogue("David starts to pull me towards our house.", thought)
        scene = 1.25

    if scene == 1.25 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Bye sweetie!", you)
        scene = 1.26

    if scene == 1.26 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Goodbye!", kristyanne)
        scene = 1.3

    if scene == 1.3 and event.type == pygame.MOUSEBUTTONUP:
        davidDoor = pygame.image.load('david and the door_1.jpg')
        screen.blit(davidDoor, (0, 0))
        pygame.display.update()
        dialogue("Mom, that was an unnecessary comment.", david)
        scene = 1.31

    if scene == 1.31 and doctor1 == True and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Unnecessary?! She seems like a good girl and you need a wife… especially now because of my condition…", you)
        scene = 1.32

    if scene == 1.31 and doctor1 == False and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Unnecessary?! She seems like a good girl and you should be looking for a woman to spend your life with. A woman who isn’t your mom.", you)
        scene = 1.32

    if scene == 1.32 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh mom… I’ll think about it.", david)
        scene = 1.33

    if scene == 1.33 and event.type == pygame.MOUSEBUTTONDOWN:
        davidCouch = pygame.image.load('david and couch_1.jpg')
        screen.blit(davidCouch, (0,0))
        pygame.display.update()
        dialogue("What was her name again?", you)
        scene = 1.34
        pygame.draw.rect(screen, (255, 255, 255), claire)
        pygame.draw.rect(screen, (255, 255, 255), catherine)
        cl = font2.render("Claire", True, (199, 167, 255))
        ca = font2.render("Catherine", True, (199, 167, 255))
        screen.blit(cl, (130, 560))
        screen.blit(ca, (305, 560))
        pygame.display.update()

    if scene == 1.34 and claire.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        scene = 1.35

    if scene == 1.34 and catherine.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        scene = 1.35

    if scene == 1.35:
        dialogue("No, it was Kristy-Anne.", david)
        scene = 1.36

    if scene == 1.36 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh… I was close enough.", you)
        if doctor1 == True:
            scene = 1.41
        else:
            scene = 1.47
    # insert 1 year later
    # after meeting kristyanne
    if scene == 1.41 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Have you been taking your medicine, mom?", david)
        scene = 1.42

    if scene == 1.42 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes, David. You remind me everyday.", you)
        scene = 1.43

    if scene == 1.43 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know. I just worry.", david)
        scene = 1.44

    if scene == 1.44 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Thank you for reminding me, sweetie.", you)
        scene = 1.45

    if scene == 1.45 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Of course.", david)
        scene = 1.47

    if scene == 1.47 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom, do you remember Kristy-Anne?", david)
        pygame.draw.rect(screen, (255, 255, 255), neighbor)
        pygame.draw.rect(screen, (255, 255, 255), gf)
        nb = font3.render("neighbor?", True, (199, 167, 255))
        gf1 = font3.render("girlfriend?", True, (199, 167, 255))
        screen.blit(nb, (112, 560))
        screen.blit(gf1, (310, 560))
        pygame.display.update()
        scene = 1.48

    if scene == 1.48 and neighbor.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        scene = 1.481

    if scene == 1.48 and gf.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        scene = 1.482

    # neighbor
    if scene == 1.481 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes.", david)
        scene = 1.4811
    if scene == 1.4811 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("What about her?", you)
        scene = 1.48111
    if scene == 1.48111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("We started dating.", david)
        scene = 1.481111
    if scene == 1.481111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("What did I tell you? I knew she’d be good for you.", you)
        scene = 1.49

    # girlfriend
    if scene == 1.482 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("How did you know?!", david)
        scene = 1.4821
    if scene == 1.4821 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Just because I’m losing my memory doesn’t mean I’m losing my mom senses.", you)
        scene = 1.49

    # pre-cactus
    if scene == 1.49 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Well, she’ll be in the house more often now.", david)
        scene = 1.491

    if scene == 1.491 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("That’s fine. It’ll be nice to have another woman in the house.", you)
        scene = 1.5

    # cactus scene
    if scene == 1.5 and event.type == pygame.MOUSEBUTTONUP:
        cactusScene = pygame.image.load('water for David Jr_1.jpg')
        screen.blit(cactusScene, (0,0))
        pygame.display.update()
        dialogue("Here you go, David Jr. You look thirsty.", you)
        scene = 1.51

    if scene == 1.51 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Did you name a cactus after me?", david)
        scene = 1.52

    if scene == 1.52 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("… no… ", you)
        scene = 1.53

    if scene == 1.53 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Really?", david)
        scene = 1.54

    if scene == 1.54 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("It’s the easiest thing to remember.", you)
        scene = 1.55

    if scene == 1.55 and event.type == pygame.MOUSEBUTTONDOWN:
        bookScene = pygame.image.load('david and david jr_1.jpg')
        screen.blit(bookScene, (0, 0))
        pygame.display.update()
        dialogue("Ok. Oh, here. I found your book.", david)
        scene = 1.56

    if scene == 1.56 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("What book?", you)
        scene = 1.57

    if scene == 1.57 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("The one you asked me to find…", david)
        scene = 1.58

    if scene == 1.58 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. That’s great! Where was it?", you)
        scene = 1.59

    if scene == 1.59 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("In the garden, you left it there.", david)
        scene = 1.511

    if scene == 1.511 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, that’s odd…", you)
        scene = 1.6

    # alarm scene
    if scene == 1.6 and event.type == pygame.MOUSEBUTTONDOWN:
        alarm = pygame.image.load('scene 5.png')
        screen.blit(alarm, (0,0))
        pygame.display.update()
        dialogue("BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP", thought)
        scene = 1.61

    if scene == 1.61 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("What the! Oh no! There’s smoke in the kitchen!", david)
        scene = 1.62

    if scene == 1.62 and event.type == pygame.MOUSEBUTTONDOWN:
        stoveScene = pygame.image.load('firing stove_1.jpg')
        screen.blit(stoveScene, (0,0))
        pygame.display.update()
        dialogue("David runs into the kitchen and I follow him. He finds a pot on the stove with smoke coming out of it. After taking care of it, he walks towards me.", thought)
        scene = 1.63

    if scene == 1.63 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom… did you leave the stove on?", david)
        pygame.draw.rect(screen, (255, 255, 255), yesStove)
        pygame.draw.rect(screen, (255, 255, 255), noStove)
        st1 = font2.render("yes", True, (199, 167, 255))
        st2 = font2.render("no", True, (199, 167, 255))
        screen.blit(st1, (150, 560))
        screen.blit(st2, (355, 560))
        pygame.display.update()
        scene = 1.64

    # Doctor: yes    stove: no
    if scene == 1.64 and yesStove.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        scene = 1.641

    if scene == 1.64 and noStove.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        scene = 1.642

    if doctor1 == True and scene == 1.641:
        dialogue("Alright. Next time tell me when you’re about to use the stove.", david)
        scene = 1.6411

    if doctor1 == True and scene == 1.6411 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I will.", you)
        scene = 1.651

    if doctor1 == True and scene == 1.651 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Thank you, mom.", david)
        scene = 1.7

    # doctor: yes    Stove: no
    if doctor1 == True and scene == 1.642:
        dialogue("Alright, I’ll go ask Kristy-Anne since she was in the house earlier.", david)
        scene = 1.6421

    if scene == 1.6421 and event.type == pygame.MOUSEBUTTONUP:
        stove = pygame.image.load('the stove_1.jpg')
        screen.blit(stove, (0, 0))
        pygame.display.update()
        dialogue("David leaves and I wait for him in the kitchen.", thought)
        scene = 1.64211

    if scene == 1.64211 and event.type == pygame.MOUSEBUTTONDOWN:
        stoveScene = pygame.image.load('firing stove_1.jpg')
        screen.blit(stoveScene, (0, 0))
        pygame.display.update()
        dialogue("Kristy-Anne said she didn’t touch the stove.", david)
        scene = 1.642111

    if scene == 1.642111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. Then I must have forgot that I was cooking something.", you)
        scene = 1.6421111

    if scene == 1.6421111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh mom… next time tell me when you’re going to use the stove.", david)
        scene = 1.64211111

    if scene == 1.64211111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok.", you)
        scene = 1.652

    if scene == 1.652 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Thank you, mom.", david)
        scene = 1.7

    # doctor: no    stove: yes
    if doctor1 == False and scene == 1.641:
        dialogue("Why didn’t you turn it off?", david)
        scene = 1.6412

    if scene == 1.6412 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I… I forgot that it was on…", you)
        scene = 1.64122

    if scene == 1.64122 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mom, let’s go to the doctor. Your memory is too bad to just be age.", david)
        scene = 1.641222

    if scene == 1.641222 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok...", you)
        scene = 1.65

    # doctor: no     stove: no
    if doctor1 == False and scene == 1.642:
        stove = pygame.image.load('the stove_1.jpg')
        screen.blit(stove, (0, 0))
        pygame.display.update()
        dialogue("Alright, I’ll go ask Kristy-Anne since she was in the house earlier.", david)
        scene = 1.6422

    if scene == 1.6422 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David leaves and I wait for him in the kitchen.", thought)
        scene = 1.64222

    if scene == 1.64222 and event.type == pygame.MOUSEBUTTONDOWN:
        screen.blit(stoveScene, (0, 0))
        pygame.display.update()
        dialogue("Kristy-Anne said she didn’t touch the stove.", david)
        scene = 1.642222

    if scene == 1.642222 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. Then I must have forgot that I was cooking something.", you)
        scene = 1.6422222

    if scene == 1.6422222 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mom, we’re going to the doctor.", david)
        scene = 1.64222222

    if scene == 1.64222222 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok...", you)
        scene = 1.65

    # doctor's office
    if scene == 1.65 and event.type == pygame.MOUSEBUTTONUP:
        doctorScene = pygame.image.load('scene 2.png')
        screen.blit(doctorScene, (0,0))
        pygame.display.update()
        dialogue("After testing, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.651

    if scene == 1.651 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("It would have been better if she had been diagnosed sooner, but here is some medication to ease the effects of the disease.", doctor)
        scene = 1.6511

    if scene == 1.6511 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Alright, thank you.", david)
        scene = 1.65111

    if scene == 1.65111 and event.type == pygame.MOUSEBUTTONDOWN:
        carScene = pygame.image.load('scene 3.png')
        screen.blit(carScene, (0,0))
        pygame.display.update()
        dialogue("David is driving us home... *did David miss a turn?*", thought)
        pygame.draw.rect(screen, (255, 255, 255), yesTurn)
        pygame.draw.rect(screen, (255, 255, 255), noTurn)
        y = font2.render("yes", True, (199, 167, 255))
        n = font2.render("no", True, (199, 167, 255))
        screen.blit(y, (150, 560))
        screen.blit(n, (355, 560))
        pygame.display.update()
        scene = 1.651111

    if scene == 1.651111 and yesTurn.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David, I think you missed a turn.", you)
        scene = 1.6511111

    if scene == 1.6511111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David ignores me...", thought)
        scene = 1.7

    if scene == 1.651111 and noTurn.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David, how much longer until we’re home?", you)
        scene = 1.6511111

    if scene == 1.6511111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("About 5 more minutes.", david)
        scene = 1.7

    if scene == 1.7 and event.type == pygame.MOUSEBUTTONUP:
        wedding = pygame.image.load('love is beautiful_1.jpg')
        screen.blit(wedding, (0,0))
        pygame.display.update()
        dialogue("David and Kristy-Anne get married two years after meeting each other. They are so wonderful together, and I’m very happy for my son :)", thought)
        scene = 1.71

    if scene == 1.71 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David’s life is the brightest it’s ever been and will only continue to be brighter. My days, on the other hand, only seem to get darker…", thought)
        scene = 2

    # ACT2 OPENING
    if scene == 2 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        act2 = font1.render("ACT TWO", True, (255, 255, 255))
        moderate = font1.render("MODERATE (5 YEARS)", True, (255, 255, 255))
        screen.blit(act2, ((500 - act2.get_width()) // 2, (600 - act2.get_height()) // 2))
        pygame.draw.line(screen, (255, 255, 255), (150, 320), (350, 320), 1)
        screen.blit(moderate, ((500 - moderate.get_width()) // 2, (600 - act2.get_height()) // 2 + 50))
        pygame.display.update()
        scene = 2.11
    # MOUSEBUTTONS ARE SUBJECT TO CHANGE
    # ACT2SCENE1(2.1)(SHANNI)
    if scene == 2.11 and (event.type == pygame.MOUSEBUTTONDOWN):
        honeymoon = pygame.image.load('back from the honeymoon_1.jpg')
        screen.blit(honeymoon, (0,0))
        pygame.display.update()
        dialogue("Mom! We’re back!", david)
        scene = 2.12
    if scene == 2.12 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh! David! Kristy-Anne! How was your honeymoon? Did you enjoy yourselves? I hope it wasn’t too short because you had to come back and take care of me…", you)
        scene = 2.13
    if scene == 2.13 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mother, don’t worry.  Our honeymoon was wonderful, and it wasn’t too short. And… we’re expecting!",kristyanne)
        scene=2.14
    if scene == 2.14 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Expecting? That means! You! I!", you)
        scene=2.15
    if scene == 2.15 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Yes mom. You’re going to have a grandchild.",david)
        scene=2.16
    if scene == 2.16 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I’m so excited!",you)
        scene=2.17
    if scene == 2.17 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("We are too. We couldn’t wait to tell you.",kristyanne)
        scene=2.18
    if scene == 2.18 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Hopefully I’ll be able to me a good grandmother. Most grandmas don’t have…",you)
        scene=2.19
    if scene == 2.19 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know you’ll be a wonderful grandma, mom.", david)
        scene=2.191
    if scene == 2.191 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Thank you.",you)
        scene=2.192
    if scene==2.192 and event.type == pygame.MOUSEBUTTONDOWN:
        screen.fill((0, 0, 0))
        scene=2.2

    # ACT2SCENE2(2.2)
    if scene == 2.2 and event.type == pygame.MOUSEBUTTONUP:
        davidDoor = pygame.image.load('david and the door_1.jpg')
        screen.blit(davidDoor, (0, 0))
        pygame.display.update()
        dialogue("Mom, where are you going?", david)
        scene = 2.21
    if scene == 2.21 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh, I was just going to go buy some groceries. I have a list so I don’t forget what I need to buy.", you)
        scene = 2.22
    if scene == 2.22 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Let me go instead. I’ll take the list and get some flowers for Kristy-Anne while I’m at it.", david)
        scene = 2.23
    if scene == 2.23 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("It’s fine, David. I need to go out so I don’t forget what the neighborhood looks like.", you)
        scene = 2.24
    if scene == 2.24 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I insist, mom. We have our daily walks for that purpose.", david)
        pygame.draw.rect(screen, [220, 220, 220], yesGroc)
        pygame.draw.rect(screen, [220, 220, 220], noGroc)
        yg1 = font3.render("Oh, alright. Get", True, (199, 167, 255))
        yg2 = font3.render("the prettiest", True, (199, 167, 255))
        yg3 = font3.render("flowers there", True, (199, 167, 255))
        screen.blit(yg1, (85, 560))
        screen.blit(yg2, (85, 580))
        screen.blit(yg3, (85, 600))
        ng1 = font3.render("Well, I insist", True, (199, 167, 255))
        ng2 = font3.render("that I go", True, (199, 167, 255))
        ng3 = font3.render("by myself", True, (199, 167, 255))
        screen.blit(ng1, (290, 560))
        screen.blit(ng2, (290, 580))
        screen.blit(ng3, (290, 600))
        pygame.display.update()
        scene = 2.25
    # LEFT
    if scene == 2.25 and yesGroc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Thank you, mom. I just don’t want you to get lost or carry the heavy groceries.", david)
        scene = 2.251
    if scene == 2.251 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("You’re the sweetest son I could ever ask for.", you)
        scene = 2.2511
    if scene == 2.2511 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("And you’re the best mom I could ask for. I’ll get my wallet, keys, and phone before heading out.", david)
        scene = 2.25111
    if scene == 2.25111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, and David. I don’t think I put this on the list, but get some of… the umm… tree looking vegetables.", you)
        scene = 2.251111
    if scene == 2.251111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("You mean broccoli?", david)
        scene = 2.2511111
    if scene == 2.2511111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes! Broccoli! It’s good for your eyes!", you)
        scene = 2.25111111
    if scene == 2.25111111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("You’re talking about carrots, mom.", david)
        scene = 2.251111111
    if scene == 2.251111111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. Then get those too.", you)
        scene = 2.2511111111
    if scene == 2.2511111111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I will, mom. I’ll ask Kristy-Anne to keep you company while I’m out.", david)
        scene = 2.2512
    if scene == 2.2512 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("You think I can’t keep myself busy? I can read my book. I don’t want to bother your wife too much since she’s due soon.", you)
        scene = 2.2513
    if scene == 2.2513 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Ok mom. I’ll be back soon.", david)
        scene = 2.2514
    if scene == 2.2514 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Bye!", you)
        scene = 2.2515
    if scene == 2.2515 and event.type == pygame.MOUSEBUTTONDOWN:
        livingRoomWKA = pygame.image.load('ka on couch_1.jpg')
        screen.blit(livingRoomWKA, (0,0))
        pygame.display.update()
        dialogue("Kristy-Anne.", you)
        scene = 2.2516
    if scene == 2.2516 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes, mother?", kristyanne)
        scene = 2.2517
    if scene == 2.2517 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Where did David go? Isn’t he usually home by this time?", you)
        scene = 2.2518
    if scene == 2.2518 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. He went to the store to buy groceries. Don’t you remember? He went instead of you.", kristyanne)
        scene = 2.2519
    if scene == 2.2519 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh… silly me. I must have forgotten. But… you don’t need to talk to me like that.", you)
        scene = 2.25191
    if scene == 2.25191 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Huh? What do you mean?", kristyanne)
        scene = 2.25192
    if scene == 2.25192 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Well, you should know by now that I’m not the best at remembering things. You shouldn’t be asking me if I remember things. Didn’t your parents teach you how to respect your in laws?", you)
        scene = 2.25193
    if scene == 2.25193 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh… I’m sorry. I didn’t mean it that way.", kristyanne)
        scene = 2.25194
    if scene == 2.25194 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know, but you should be more careful of what you say.", you)
        scene = 2.25195
    if scene == 2.25195 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok… David should be here any moment now.", kristyanne)
        scene = 2.25196
    if scene == 2.25196 and event.type == pygame.MOUSEBUTTONDOWN:
        davidAndKA = pygame.image.load('david and ka and couch_1.jpg')
        screen.blit(davidAndKA, (0, 0))
        pygame.display.update()
        dialogue("I’m home!", david)
        scene = 2.25197
    if scene == 2.25197 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David! Welcome home! Kristy-Anne and I were just having a pleasant conversation.", you)
        scene = 2.25198
    if scene == 2.25198 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mhm. Pleasant. Your mother really missed you.", kristyanne)
        scene = 2.25199
    if scene == 2.25199 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, mom. I was only at the store.", david)
        scene = 2.25181
    if scene == 2.25181 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know but I sort of… forgot.", you)
        scene = 2.25182
    if scene == 2.25182 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David. Could I… speak to you for a second?", kristyanne)
        scene = 2.25183
    if scene == 2.25183 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Of course, dear.", david)
        scene = 2.25184
    if scene == 2.25184 and event.type == pygame.MOUSEBUTTONUP:
        empty = pygame.image.load('empty couch_1.jpg')
        screen.blit(empty, (0, 0))
        pygame.display.update()
        dialogue("David and Kristy-Anne walk into another room. I can’t hear the things they’re saying, but it probably has to do with my memory loss. Or maybe she is unhappy with the conversation we just had. Oh… I suppose it was a little uncalled for…", thought)
        scene = 2.25185
    if scene == 2.25185 and event.type == pygame.MOUSEBUTTONDOWN:
        davidCouch = pygame.image.load('david and couch_1.jpg')
        screen.blit(davidCouch, (0, 0))
        pygame.display.update()
        dialogue("Mom?", david)
        scene = 2.25186
    if scene == 2.25186 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David’s voice breaks my thoughts.", thought)
        scene = 2.25187
    if scene == 2.25187 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Yes, David?", you)
        scene = 2.25188
    if scene == 2.25188 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I want you to get along with Kristy-Anne. You used to always dote on her.", david)
        scene = 2.25189
    if scene == 2.25189 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know David… I’m not sure what’s wrong with me lately.", you)
        scene = 2.25171
    if scene == 2.25171 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Well, I know you’re a caring person, mom. I don’t think this condition will change that.", david)
        scene = 2.25172
    if scene == 2.25172 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I hope not, David. I hope not…", you)
        scene = 2.3

    # RIGHT
    if scene == 2.25 and noGroc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh… ok. Just… give me a call if you need anything.",david)
        scene=2.2521
    if scene==2.2521 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Oh. I didn’t mean to sound harsh. But I will give you a call. Thank you, sweetie.",you)
        scene=2.2522
    if scene==2.2522 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("I just want you to be safe, mom.",david)
        scene=2.2523
    if scene==2.2523 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I will be safe. The neighbors know about my condition. Plus you’re always one call away.",you)
        scene=2.2524
    if scene==2.2524 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("I know. I suppose I worry a bit too much. You have your wallet and phone?",david)
        scene=2.2525
    if scene==2.2525 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Yes, David. I take extra care to have everything I need before I go out.",you)
        scene=2.2526
    if scene==2.2526 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Ok, mom. I’ll see you soon.",david)
        scene=2.2527
    if scene==2.2527 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Bye",you)
        scene=2.253
    if scene==2.253 and event.type==pygame.MOUSEBUTTONDOWN:
        street = pygame.image.load('street.jpg')
        screen.blit(street, (0,0))
        pygame.display.update()
        dialogue("Hmm… I can’t seem to recall where I am now… Oh dear. Am I lost? That isn’t good…",thought)
        scene = 2.25331
    if scene == 2.25331 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Do I make a right here? Or is it a left? Maybe I should call David… he’ll know what to do.", thought)
        scene = 2.25332
    if scene == 2.25332 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Should I call David?", thought)
        pygame.draw.rect(screen, (220, 220, 220), yesCall)
        pygame.draw.rect(screen, (220, 220, 220), noCall)
        call = font2.render("Call", True, (199, 167, 255))
        dCall = font2.render("Don't Call", True, (199, 167, 255))
        screen.blit(call, (130, 560))
        screen.blit(dCall, (305, 560))
        pygame.display.update()
        scene=2.2531
    if scene==2.2531 and yesCall.collidepoint(mousePos)and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I should call David. I did tell him I’d call him if anything happened. He won’t be too happy if he finds out I continued to wander around when I wasn’t sure where I was. The phone rings for a bit before I hear David’s voice.",thought)
        scene=2.25312
    if scene==2.25312 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Hello? Mom?",david)
        scene=2.253122
    if scene==2.253122 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("David! I uh… can’t seem to recall where I am.",you)
        scene=2.2531222
    if scene==2.2531222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Oh. Tell me what street you’re on and I’ll come pick you up.",david)
        scene=2.25312222
    if scene==2.25312222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("But the groceries…",you)
        scene=2.253122222
    if scene==2.253122222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("It’s ok, mom. We can get them together.",david)
        scene=2.2531222222
    if scene==2.2531222222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Ok. I’m on… Green Street and Apple Avenue.",you)
        scene=2.25312222222
    if scene==2.25312222222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("I'll be right there.",david)
        scene=2.2532
    if scene==2.2531 and noCall.collidepoint(mousePos)and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I don’t need to call David, I’ll be alright. I’ve been on this route multiple times. I’ll get to the store through muscle memory.",thought)
        scene=2.25313
    if scene==2.25313 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("I continue to try to find my way to the store, gripping my list tightly when I hear a car horn. I turn and see David in his car.",thought)
        scene=2.253133
    if scene==2.253133 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("David?",you)
        scene=2.2531333
    if scene==2.2531333 and event.type==pygame.MOUSEBUTTONDOWN:
        davidCar = pygame.image.load('david by car.jpg')
        screen.blit(davidCar, (0, 0))
        pygame.display.update()
        dialogue("Yes mom. I’m here to pick you up.",david)
        scene=2.25313333
    if scene==2.25313333 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("H-how did you know where I was?",you)
        scene=2.253133333
    if scene==2.253133333 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("A neighbor called and told me he saw you wandering around.",david)
        scene=2.25314
    if scene==2.25314 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("But… I’m on my way to the store.",you)
        scene=2.253144
    if scene==2.253144 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("This isn’t the way to the store, mom. That’s why he called.",david)
        scene=2.2531444
    if scene==2.2531444 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Oh… I’ll get in the car.",you)
        scene=2.25314444
    if scene==2.25314444 and event.type==pygame.MOUSEBUTTONDOWN:
        carScene = pygame.image.load('scene 3.png')
        screen.blit(carScene, (0, 0))
        pygame.display.update()
        dialogue("Thank you, mom. Let’s get you home.",david)
        scene=2.253144444
    if scene==2.253144444 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("But… the groceries…",you)
        scene=2.2531444444
    if scene==2.2531444444 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Hmm… alright, let’s go to the store first since we’re already out.",david)
        scene=2.2532
    if scene==2.2532 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("We sit in silence as David drives to the store.",thought)
        scene=2.25322
    if scene==2.25322 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Mom, next time, let me handle the groceries. Or let me go with you at least.",david)
        scene=2.253222
    if scene==2.253222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Ok. I’m sorry for causing you trouble.",you)
        scene=2.2532222
    if scene==2.2532222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("It’s ok, mom. I just want you to be safe.",david)
        scene=2.25322222
    if scene==2.25322222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I know… I know.",you)
        scene=2.3

    # ACT2SCENE3(2.3)(SHANNI)
    if scene==2.3 and event.type==pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        scene=2.31
    if scene == 2.31 and event.type==pygame.MOUSEBUTTONDOWN:
        pygame.display.update()
        dialogue("Mom! Mom, we’re home! We have a son! Did you hear that? You have a grandson!",david)
        scene=2.311
    if scene==2.311 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Where is she? She usually greets us at the door. Do you think she’s hurt? Lost?",kristyanne)
        scene=2.3111
    if scene == 2.3111 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Let’s check her room. Maybe she’s waiting for us there.Mom? Mom, wake up.",david)
        scene=2.32
    if scene==2.32 and event.type==pygame.MOUSEBUTTONUP:
        jacobBorn = pygame.image.load('jacob is born_1.jpg')
        screen.blit(jacobBorn, (0, 0))
        pygame.display.update()
        dialogue("Huh? Is it morning already?",you)
        scene=2.322
    if scene==2.322 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("No, mom. It’s 4 in the afternoon.",david)
        scene=2.3222
    if scene==2.3222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("4? All I know is I was really tired, so I went to bed. I don’t remember what time I slept though…",you)
        scene=2.32222
    if scene==2.32222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Well, at least you’re up. Meet your grandson, Jacob! Isn’t he adorable?",kristyanne)
        scene=2.3222222
    if scene==2.3222222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Oh! He looks just like David when he was born. Oh, but he has your nose,  Kristy-Anne.",you)
        scene=2.32222222
    if scene==2.32222222 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("David, I’m tired. I’ll take Jacob with me and put him in his crib. I should rest now so I’ll be able to take care of Jacob when he wakes up later.",kristyanne)
        scene=2.322222222
    if scene==2.322222222 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Ok, dear. I’ll leave you to rest.",david)
        scene=2.33
    if scene==2.33 and event.type==pygame.MOUSEBUTTONDOWN:
        davidDoor = pygame.image.load('david and the door_1.jpg')
        screen.blit(davidDoor, (0, 0))
        pygame.display.update()
        dialogue("Mom, are you alright?",david)
        scene=2.333
    if scene==2.333 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Yes, of course I am. I was just taking a nap.",you)
        scene=2.3333
    if scene==2.3333 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("But mom, you usually don’t take naps.",david)
        scene=2.33333
    if scene==2.33333 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I know… I just…",you)
        scene=2.333333
    if scene==2.333333 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Are you sure you’re feeling alright?",david)
        scene=2.3333333
    if scene==2.3333333 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Well, I haven’t been able to sleep at night and I’ve been feeling terribly sleepy in the morning.",you)
        scene=2.33333333
    if scene==2.33333333 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Oh… well, why don’t you go back to sleep and I’ll call the doctor to ask what might be wrong.",david)
        scene=2.333333333
    if scene==2.333333333 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I don’t think so… I haven’t been able to sleep at night lately.",you)
        scene=2.3333333333
    if scene==2.3333333333 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("You haven’t?",david)
        scene=2.37
    if scene==2.37 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I haven’t.",you)
        scene=2.377
    if scene==2.377 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Why didn’t you tell me?",david)
        scene=2.3777
    if scene==2.3777 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("I didn’t think it was a big deal and I didn’t want you to stress more than you needed to, especially since you had a baby on the way.",you)
        scene=2.37777
    if scene==2.37777 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("Oh mom… you should go back to sleep. I’ll call the doctor to ask what might be wrong.",david)
        scene=2.377777
    if scene==2.377777 and event.type==pygame.MOUSEBUTTONUP:
        dialogue("Ok David",you)
        scene=2.38
    if scene==2.38 and event.type==pygame.MOUSEBUTTONDOWN:
        dialogue("I close my eyes as he leaves the room. I don’t want him to worry so much, but I’m too tired to reassure him any more.",thought)
        scene=2.4

    # ACT2SCENE4(2.4)(VIVIAN)
    if scene == 2.4 and event.type == pygame.MOUSEBUTTONUP:
        closet = pygame.image.load('bad closet_1.jpg')
        screen.blit(closet, (0, 0))
        pygame.display.update()
        dialogue("Kristy-Anne! Could you come to my room for a bit?", you)
        scene = 2.41
    if scene == 2.41 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("After a couple of minutes after I call her name, I hear the door to the bedroom creak open.", thought)
        scene = 2.42
    if scene == 2.42 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes, mother?", kristyanne)
        scene = 2.43
    if scene == 2.43 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Over here, in the closet.", you)
        scene = 2.44
    if scene == 2.44 and event.type == pygame.MOUSEBUTTONUP:
        peekingka = pygame.image.load('peaking ka_1.jpg')
        screen.blit(peekingka, (0, 0))
        pygame.display.update()
        dialogue("What are you doing here, mother?", kristyanne)
        scene = 2.45
    if scene == 2.45 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mmm… I didn’t want to ask David… but could you help me choose out some clothes for the day? I’m not sure what to wear…", you)
        scene = 2.46
    if scene == 2.46 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, of course I can.", kristyanne)
        scene = 2.47
    if scene == 2.47 and event.type == pygame.MOUSEBUTTONDOWN:
        clothes = pygame.image.load('skirt cameo_1.jpg')
        screen.blit(clothes, (0, 0))
        pygame.display.update()
        dialogue("After a few minutes of her rummaging through my closet, she sets down an outfit on my bed.", thought)
        scene = 2.48
    if scene == 2.48 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh! It’s wonderful! Thank you so much, dear.", you)
        scene = 2.49
    if scene == 2.49 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Don’t mention it. Would you like me to do this everyday from now on?", kristyanne)
        pygame.draw.rect(screen, (220, 220, 220), yesHelp)
        pygame.draw.rect(screen, (220, 220, 220), noHelp)
        yh = font2.render("yes", True, (199, 167, 255))
        nh = font2.render("no", True, (199, 167, 255))
        screen.blit(yh, (120, 560))
        screen.blit(nh, (325, 560))
        pygame.display.update()
        scene = 2.411
    if scene == 2.411 and yesHelp.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok, I can do that.", kristyanne)
        scene = 2.4111
    if scene == 2.4111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Kristy-Anne at your service ;)", kristyanne)
        scene = 2.413
    if scene == 2.411 and noHelp.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I insist, mother. Please? It’ll be easier than asking me everyday if I just do it myself.", you)
        scene = 2.4112
    if scene == 2.4112 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Are you sure it won’t be too much trouble?", you)
        scene = 2.41122
    if scene == 2.41122 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("It won’t. I’ll take that as a yes!", kristyanne)
        scene = 2.413
    if scene == 2.413 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Thank you, Kristy-Anne.", you)
        scene = 2.414
    if scene == 2.414 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("It’s the least I can do.", kristyanne)
        scene = 2.415
    if scene == 2.415 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("As she leaves, I stare at the clothes she laid out for me. I can’t even choose my own clothes anymore… what has become of me?", thought)
        scene = 2.5

    # ACT2SCENE5(2.5)(VIVIAN)
    if scene == 2.5 and event.type == pygame.MOUSEBUTTONDOWN:
        tissueD = pygame.image.load('david with tissue.jpg')
        screen.blit(tissueD, (0, 0))
        pygame.display.update()
        dialogue("Mom! What are you doing?! You made a mess!", david)
        scene = 2.51
    if scene == 2.51 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh. I didn’t notice! It just- I- it’s calming…", you)
        scene = 2.52
    if scene == 2.52 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh mom… I have to clean this up now…", david)
        scene = 2.53
    if scene == 2.53 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("You don’t think I can clean up after myself?", you)
        scene = 2.54
    if scene == 2.54 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("What? No, that’s not what I mean.", david)
        scene = 2.55
    if scene == 2.55 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Well, that’s what it sounds like. What’s so wrong with some… some… shredded tissue? I’m so sorry that I… that… I get calm from making a mess.", you)
        scene = 2.56
    if scene == 2.56 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mom! Why are you like this? You know that’s not true.", david)
        scene = 2.57
    if scene == 2.57 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I’m about to say something when a load wail from David and Kristy-Anne’s room interrupts us.", thought)
        scene = 2.58
    if scene == 2.58 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Jacob! Go check on him, David!", you)
        scene = 2.59
    if scene == 2.59 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("He probably got upset by our argument. I’m sorry mom. I’ll go check on him.", david)
        scene = 2.511
    if scene == 2.511 and event.type == pygame.MOUSEBUTTONDOWN:
        tissues = pygame.image.load('tissue couch_1.jpg')
        screen.blit(tissues, (0, 0))
        pygame.display.update()
        dialogue("As David runs off, I sit back down and stare at my pile of shredded tissue.", thought)
        scene = 2.512
    if scene == 2.512 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I suppose I shouldn’t have done this… I should… should… what’s the word… let’s get rid of it. I’m sorry David… I’m a mess… just like this one…", thought)
        scene = 2.6

    # ACT2SCENE6(2.6)(SEONGA)
    if scene == 2.6 and event.type == pygame.MOUSEBUTTONDOWN:
        jacobLeaf = pygame.image.load('jacob and the leaf_1.jpg')
        screen.blit(jacobLeaf, (0, 0))
        pygame.display.update()
        dialogue("Jacob! Don’t eat that! That’s dirty!", you)
        scene = 2.61

    if scene == 2.61 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("But… yummy!", jacob)
        scene = 2.62

    if scene == 2.62 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David no!", you)
        scene = 2.63

    if scene == 2.63 and event.type == pygame.MOUSEBUTTONUP:
        jacobConf = pygame.image.load('jacob and the questions_1.jpg')
        screen.blit(jacobConf, (0, 0))
        pygame.display.update()
        dialogue("Day bid?... dada?", jacob)
        scene = 2.64

    if scene == 2.63 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh… where is your dad?", you)
        scene = 2.64

    if scene == 2.64 and event.type == pygame.MOUSEBUTTONUP:
        davidDoor = pygame.image.load('david and the door_1.jpg')
        screen.blit(davidDoor, (0, 0))
        pygame.display.update()
        dialogue("Mom? Did you call me?", david)
        scene = 2.65

    if scene == 2.65 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Huh? Who are you? I’m just spending time with my son. But… I don’t know where his father is…", you)
        scene = 2.66

    if scene == 2.66 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Dada! Up! Up!", jacob)
        scene = 2.67

    if scene == 2.67 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Mom… this is my son… I’m your son, David… he’s your grandson… dad… your husband… died seven years ago in a car accident…", david)
        scene = 2.68

    if scene == 2.68 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("What? David? What’s going on?", you)
        scene = 2.69

    if scene == 2.69 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I don’t know mom… I think you should go inside...", david)
        scene = 2.7

    # ACT2SCENE7(2.7)(SEONGA)
    if scene == 2.7 and event.type == pygame.MOUSEBUTTONUP:
        dande = pygame.image.load('meet ellen.jpg')
        screen.blit(dande, (0, 0))
        pygame.display.update()
        dialogue("Mom, I want you to meet someone.", david)
        scene = 2.71

    if scene == 2.71 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Who? Her?", you)
        scene = 2.72

    if scene == 2.72 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes, mom. She’s going to be your personal helper from now on.", david)
        scene = 2.73

    if scene == 2.73 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Oh…", you)
        pygame.draw.rect(screen, (220, 220, 220), yesHelp1)
        pygame.draw.rect(screen, (220, 220, 220), noHelp1)
        yh1 = font3.render("Thank you..", True, (199, 167, 255))
        nh1 = font3.render("I don't", True, (199, 167, 255))
        nh2 = font3.render("need her.", True, (199, 167, 255))
        screen.blit(yh1, (120, 570))
        screen.blit(nh1, (330, 560))
        screen.blit(nh2, (335, 580))
        pygame.display.update()
        scene = 2.74

    if scene == 2.74 and yesHelp1.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Hello, my name is Ellen. I’ll be assisting you from now on.", unknown)
        scene = 2.742

    if scene == 2.742 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Will you be living here?", you)
        scene = 2.7422

    if scene == 2.7422 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("No, I’ll only stay until 7 in the evening and arrive at 6 in the morning.", ellen)
        scene = 2.74222

    if scene == 2.742222 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("She is only going to be here when Kristy-Anne and I are at work and a little longer.", david)
        scene = 2.75

    if scene == 2.74 and noHelp1.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom, that’s rude. We already hired her. You should be grateful.", david)
        scene = 2.741

    if scene == 2.741 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Fine.", you)
        scene = 2.74111

    if scene == 2.74111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Umm… my name is Ellen. I’ll be assisting you from now on.", unknown)
        scene = 2.741111

    if scene == 2.741111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("She’ll only be here when Kristy-Anne and I are at work. We’re just worried for you.", david)
        scene = 2.75

    if scene == 2.75 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok...", you)
        scene = 2.76

    if scene == 2.76 and event.type == pygame.MOUSEBUTTONDOWN:
        empty = pygame.image.load('empty couch_1.jpg')
        screen.blit(empty, (0, 0))
        pygame.display.update()
        dialogue("I’m sorry David. I must be such a huge burden on you… If only I could be a better mother…", thought)
        scene = 3

     # ACT THREE
    if scene == 3 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        act3 = font1.render("ACT THREE", True, (255, 255, 255))
        severe = font1.render("SEVERE (1 YEARS)", True, (255, 255, 255))
        screen.blit(act3, ((500 - act3.get_width()) // 2, (600 - act3.get_height()) // 2))
        pygame.draw.line(screen, (255, 255, 255), (150, 320), (350, 320), 1)
        screen.blit(severe, ((500 - severe.get_width()) // 2, (600 - act3.get_height()) // 2 + 50))
        pygame.display.update()
        scene = 3.1

    # ACT3SCENE1 (3.1)
    if scene == 3.1 and event.type == pygame.MOUSEBUTTONDOWN:
        wheelchair = pygame.image.load('wheelchair.jpg')
        screen.blit(wheelchair, (0, 0))
        pygame.display.update()
        dialogue("Mom, I got you a wheelchair. It’ll be easier to move around.", david)
        scene = 3.12

    if scene == 3.12 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Thanks. Should easy. Difficult to walk me.", you)
        scene = 3.13

    if scene == 3.13 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("I know. Ellen told me.", david)
        scene = 3.14

    if scene == 3.14 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Who?", you)
        scene = 3.15

    if scene == 3.15 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Ellen, mom. Your personal helper.", david)
        scene = 3.16

    if scene == 3.16 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, strange woman walk with me and food?", you)
        scene = 3.17

    if scene == 3.17 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Yes mom…", david)
        scene = 3.18

    if scene == 3.18 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Tired. Go bed.", you)
        scene = 3.19

    if scene == 3.19 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Ok mom. Let’s get you to bed so you can sleep.", david)
        scene = 3.111

    if scene == 3.111 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        pygame.display.update()
        dialogue("I’m sorry David… I can’t do anything for you anymore, but you need to do everything for me. I wish I could turn back time to when things were easier…", thought)
        scene = 3.2

    # ACT3SCENE2
    if scene == 3.2 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Sobbing noises wake me up.", thought)
        scene = 3.21

    if scene == 3.21 and event.type == pygame.MOUSEBUTTONUP:
        crying2 = pygame.image.load('jacob crying david_1.jpg')
        screen.blit(crying2, (0, 0))
        pygame.display.update()
        dialogue("Dada, don’t cry…", jacob)
        scene = 3.22

    if scene == 3.22 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Ah, I’m sorry Jacob. Your dad should be a strong man. You shouldn’t have to see your dad crying and broken.", david)
        scene = 3.23

    if scene == 3.23 and event.type == pygame.MOUSEBUTTONUP:
        crying3 = pygame.image.load('everyone crying_1.jpg')
        screen.blit(crying3, (0, 0))
        pygame.display.update()
        dialogue("David, don’t say that. It’s because she’s your mom.", unknown)
        scene = 3.24

    if scene == 3.24 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Dada is sad because of grandma?", unknown)
        scene = 3.25

    if scene == 3.25 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Yes Jacob. Your grandma is very sick, and your dad loves her very much.", david)
        scene = 3.26

    if scene == 3.26 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Jacob… it’s bedtime. Let’s go to your room.", unknown)
        scene = 3.27

    if scene == 3.27 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok mama… goodnight dada. I love you.", unknown)
        scene = 3.28

    if scene == 3.28 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Goodnight Jacob. Sleep tight.", david)
        scene = 3.29

    if scene == 3.29 and event.type == pygame.MOUSEBUTTONUP:
        crying = pygame.image.load('crying david_1.jpg')
        screen.blit(crying, (0, 0))
        pygame.display.update()
        dialogue("Footsteps walk away from where we are.", thought)
        scene = 3.211

    if scene == 3.211 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Da…", you)
        scene = 3.212

    if scene == 3.212 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        pygame.display.update()
        dialogue("Mom? Are you awake?", david)
        scene = 3.213

    if scene == 3.213 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Eh… meh… sss…", you)
        scene = 3.214

    if scene == 3.214 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("I’m sorry, David. Seeing me like this must make you so sad and tired. I only wanted you to have a happy and healthy life.", thought)
        scene = 3.3

    # ACT3SCENE3
    if scene == 3.3 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("There’s nothing… breathing is hard… how long has it been… I’m tired… I think…", thought)
        scene = 3.31

    if scene == 3.31 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom… please… just one answer... Please… you can’t leave, not yet… I’m not ready for that…", unknown)
        scene = 3.32

    if scene == 3.32 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Who? A strange man is at the side of my bed.", thought)
        scene = 3.33

    if scene == 3.33 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom… I love you… I always will…", unknown)
        scene = 3.34

    if scene == 3.34 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("This man… he’s important to me. His voice makes my heart happy. But I can’t remember… who is he? Oh, that’s right.", thought)
        scene = 3.35

    if scene == 3.35 and event.type == pygame.MOUSEBUTTONUP:
        end1 = pygame.image.load('mmexport1565742125774.jpg')
        screen.blit(end1, (0,0))
        pygame.display.update()
        dialogue("David", thought)
        scene = 3.36

    if scene == 3.36 and event.type == pygame.MOUSEBUTTONDOWN:
        end2 = pygame.image.load('mmexport1565737402067.jpg')
        screen.blit(end2, (0,0))
        pygame.display.update()
        dialogue("I wish I could tell you... ", thought)
        scene = 3.37

    if scene == 3.37 and event.type == pygame.MOUSEBUTTONUP:
        end3 = pygame.image.load('mmexport1565737404135.jpg')
        screen.blit(end3, (0,0))
        pygame.display.update()
        dialogue("how much I love you", thought)
        scene = 4

    # ENDING CREDITS (4)
    if scene == 4 and event.type == pygame.MOUSEBUTTONDOWN:
        screen.fill((0, 0, 0))
        dialogueCredit("Alzheimer’s is a disease that affects the brain, causing the patient to lose their memory as well as basic function, such as speech, walking, and eating.                                      Treat your family members with this disease with love and patience.")
        scene = 4.1

    if scene == 4.1 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        ribbon = pygame.image.load('alzRibbon.png')
        screen.blit(ribbon, ((500 - ribbon.get_width()) // 2, 330))
        credit = font2.render("Credits: ", True, (255, 255, 255))
        v = font2.render("Vivian Chen Lam",True, (255, 255, 255))
        se = font2.render("Seonga Oh", True, (255, 255, 255))
        sh = font2.render("Shanni Yu", True, (255, 255, 255))
        spec = font2.render("Special thanks to:", True, (255, 255, 255))
        r = font2.render("Ronnie", True, (255, 255, 255))
        j = font2.render("Jess", True, (255, 255, 255))
        heart = font2.render("<3", True, (255, 0, 0))
        screen.blit(credit, ((500 - credit.get_width()) // 2, 70))
        screen.blit(v, ((500 - v.get_width()) // 2, 100))
        screen.blit(se, ((500 - se.get_width()) // 2, 130))
        screen.blit(sh, ((500 - sh.get_width()) // 2, 160))
        screen.blit(spec, ((500 - spec.get_width()) // 2, 210))
        screen.blit(r, ((500 - r.get_width()) // 2, 240))
        screen.blit(j, ((500 - j.get_width()) // 2, 270))
        screen.blit(heart, ((500 - heart.get_width()) // 2, 300))
        pygame.display.update()
