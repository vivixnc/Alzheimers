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
# inserting image
#David1 = pygame.image.load('david1.png')
#gameDisplay.blit(David1, (x,y))

# Fonts
font1 = pygame.font.SysFont("Monospace", 30)
font2 = pygame.font.SysFont("Monospace", 20)
font3 = pygame.font.SysFont("Monospace", 15)

# sets scene to 0
scene = 0.0

# words for opening page
title = font1.render("Alzheimer's", True, (56, 0, 113))
start = font2.render("click anywhere to continue", True, (56, 0, 113))

# instantiating names for dialogue, **colors are subject to change**
you = font2.render("You: ", True, (255, 255, 255))
david = font2.render("David: ", True, (255, 255, 255))
preka = font2.render("???: ", True, (255, 255, 255))
kristyanne = font2.render("Kristy-Anne: ", True, (255, 255, 255))
doctor = font2.render("Dr. Pineapple: ", True, (255, 255, 255))
thought = font2.render(" ", True, (255, 255, 255))
# making yes and no buttons for act one scene 1
yesDoc = pygame.Rect(75, 550, 150, 80)
noDoc = pygame.Rect(275, 550, 150, 80)
yesTurn = pygame.Rect(100, 550, 130, 50)
noTurn = pygame.Rect(300, 550, 130, 50)
claire = pygame.Rect(100, 550, 130, 50)
catherine = pygame.Rect(300, 550, 130, 50)
neighbor = pygame.Rect(100, 550, 130, 50)
gf = pygame.Rect(300, 550, 130, 50)
yesStove = pygame.Rect(100, 550, 150, 80)
noStove = pygame.Rect(300, 550, 150, 80)

done = False

def dialogue(line, speaker):
    pygame.draw.rect(screen, (20, 0, 56), (0, 400, 500, 700), 0)
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
        letter = font3.render(line[i], True, (255, 255, 255))
        screen.blit(letter, (x, y))
        pygame.display.flip()
        pygame.time.wait(30)
    pygame.mixer.music.stop()

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
        screen.fill((0, 0, 0))
        screen.blit(title, ((500 - title.get_width()) // 2, (600 - title.get_height()) // 2))
        screen.blit(start, ((500 - start.get_width()) // 2, (600 - start.get_height()) // 2 + 30))
        pygame.display.update()

    # when the user clicks opening screen
    # act 1 opening screen appears
    if(scene == 0.0 and event.type == pygame.MOUSEBUTTONUP):
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
        dialogue("Mom, let's go to the doctor to check up on your health. I've noticed your memory has been a little off lately......", david)

        # drawing yes and no buttons (box only)
        pygame.draw.rect(screen, [0, 0, 0], yesDoc)
        pygame.draw.rect(screen, [0, 0, 0], noDoc)

        # rendering and printing button text
        yes1 = font3.render("yes, i should", True, (255, 255, 255))
        yes2 = font3.render("probably get it", True, (255, 255, 255))
        yes3 = font3.render("checked :/", True, (255, 255, 255))
        screen.blit(yes1, (85, 560))
        screen.blit(yes2, (85, 580))
        screen.blit(yes3, (85, 600))
        no1 = font3.render("no, i'm not", True, (255, 255, 255))
        no2 = font3.render("going insane", True, (255, 255, 255))
        no3 = font3.render(">:(", True, (255, 255, 255))
        screen.blit(no1, (300, 560))
        screen.blit(no2, (295, 580))
        screen.blit(no3, (330, 600))
        pygame.display.update()
        scene= 1.01
    # what happens when the player chooses yes
    # diagnosis
    if scene == 1.01 and yesDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("After testing, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.11
    # medication
    if scene == 1.11 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("As you may know, there is no cure for Alzheimer’s but there is medication to slow down the process.", doctor)
        scene = 1.111
    # leaving doctor's office
    if scene == 1.111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Alright, thank you.", david)
        scene = 1.1111
    # car scene/going home
    if scene == 1.1111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("*did David miss a turn?*", you)
        pygame.draw.rect(screen, (0, 0, 0), yesTurn)
        pygame.draw.rect(screen, (0, 0, 0), noTurn)
        y = font2.render("yes", True, (255, 255, 255))
        n = font2.render("no", True, (255, 255, 255))
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
        dialogue("Oh hello! You must be my new neighbors. My name is Kristy-Anne. I just moved in next door.", preka)
        scene = 1.21

    if scene == 1.21 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Hello! It’s nice to see a new face around here. You like a good woman to be in my David’s life.", you)
        scene = 1.22

    if scene == 1.22 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David’s face turns red and the girl giggles.", thought)
        scene = 1.23

    if scene == 1.23 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom! You must be tired. Let’s get you inside.", david)
        scene = 1.24

    if scene == 1.24 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David starts to pull me towards our house.", thought)
        scene = 1.25

    if scene == 1.25 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Bye sweetie!", you)
        scene = 1.26

    if scene == 1.26 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Goodbye!", kristyanne)
        scene = 1.3

    if scene == 1.3 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom, that was an unnecessary comment.", david)
        scene = 1.31

    if scene == 1.31 and doctor1 == True and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("Unnecessary?! She seems like a good girl and you need a wife… especially now because of my condition…", you)
        scene = 1.32

    if scene == 1.31 and doctor1 == False and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Unnecessary?! She seems like a good girl and you should be looking for a woman to spend your life with. A woman who isn’t your mom.", you)
        scene = 1.32

    if scene == 1.32 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh mom… I’ll think about it.", david)
        scene = 1.33

    if scene == 1.33 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("What was her name again?", you)
        scene = 1.34
        pygame.draw.rect(screen, (0, 0, 0), claire)
        pygame.draw.rect(screen, (0, 0, 0), catherine)
        cl = font2.render("Claire", True, (255, 255, 255))
        ca = font2.render("Catherine", True, (255, 255, 255))
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
        pygame.draw.rect(screen, (0, 0, 0), neighbor)
        pygame.draw.rect(screen, (0, 0, 0), gf)
        nb = font3.render("our neighbor?", True, (255, 255, 255))
        gf1 = font3.render("your girlfriend?", True, (255, 255, 255))
        screen.blit(nb, (120, 560))
        screen.blit(gf1, (325, 560))
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
        dialogue("BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP BEEP", thought)
        scene = 1.61

    if scene == 1.61 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("What the! Oh no! There’s smoke in the kitchen!", david)
        scene = 1.62

    if scene == 1.62 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David runs into the kitchen and I follow him. He finds a pot on the stove with smoke coming out of it. After taking care of it, he walks towards me.", thought)
        scene = 1.63

    if scene == 1.63 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Mom… did you leave the stove on?", david)
        pygame.draw.rect(screen, (0, 0, 0), yesStove)
        pygame.draw.rect(screen, (0, 0, 0), noStove)
        st1 = font2.render("yes", True, (255, 255, 255))
        st2 = font2.render("no", True, (255, 255, 255))
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
        dialogue("David leaves and I wait for him in the kitchen.", thought)
        scene = 1.64211

    if scene == 1.64211 and event.type == pygame.MOUSEBUTTONDOWN:
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
        dialogue("Alright, I’ll go ask Kristy-Anne since she was in the house earlier.", david)
        scene = 1.6422

    if scene == 1.6422 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("David leaves and I wait for him in the kitchen.", thought)
        scene = 1.64222

    if scene == 1.64222 and event.type == pygame.MOUSEBUTTONDOWN:
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
        dialogue("After testing, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.651

    if scene == 1.651 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("It would have been better if she had been diagnosed sooner, but here is some medication to ease the effects of the disease.", doctor)
        scene = 1.6511

    if scene == 1.6511 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Alright, thank you.", david)
        scene = 1.65111

    if scene == 1.65111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David is driving us home... *did David miss a turn?*", thought)
        pygame.draw.rect(screen, (0, 0, 0), yesTurn)
        pygame.draw.rect(screen, (0, 0, 0), noTurn)
        y = font2.render("yes", True, (255, 255, 255))
        n = font2.render("no", True, (255, 255, 255))
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
        dialogue("David and Kristy-Anne get married two years after meeting each other. They are so wonderful together, and I’m very happy for my son :)", thought)
        scene == 1.71

    if scene == 1.71 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("David’s life is the brightest it’s ever been and will only continue to be brighter. My days, on the other hand, only seem to get darker…", thought)
        scene = 2

    # ACT2 OPENING
    if scene == 2 and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 0, 0))
        act2 = font1.render("ACT TWO", True, (255, 255, 255))
        moderate = font1.render("MODERATE (5 YEARS)", True, (255, 255, 255))
        screen.blit(act1, ((500 - act2.get_width()) // 2, (600 - act2.get_height()) // 2))
        pygame.draw.line(screen, (255, 255, 255), (150, 320), (350, 320), 1)
        screen.blit(mid, ((500 - moderate.get_width()) // 2, (600 - act2.get_height()) // 2 + 50))
        pygame.display.update()
        scene = 2.1

    # ACT2SCENE1(2.1)

    # ACT2SCENE2(2.2)

    # ACT2SCENE3(2.3)

    # ACT2SCENE4(2.4)

    # ACT2SCENE5(2.5)

    # ACT2SCENE6(2.6)

    # ACT2SCENE7(2.7)
