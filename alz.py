import pygame
import sys
# https://www.soundjay.com/communication-sounds.html
# second track
# setting up window
pygame.init()
screen = pygame.display.set_mode((500,650))
pygame.display.set_caption("Alzhemier's")
clock = pygame.time.Clock()

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
kristyanne = font2.render("Kristy-Anne: ", True, (255, 255, 255))
doctor = font2.render("Dr. Pineapple: ", True, (255, 255, 255))

# making yes and no buttons for act one scene 1
yesDoc = pygame.Rect(75, 550, 150, 80)
noDoc = pygame.Rect(275, 550, 150, 80)
yesTurn = pygame.Rect(100, 550, 130, 50)
noTurn = pygame.Rect(300, 550, 130, 50)

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
        if(x >= 450 and line[i-1] == " "):
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
        dialogue("I am sorry to inform you that your mother has been diagnosed with Alzheimer's.", doctor)
        scene = 1.11
    # medication
    if scene == 1.11 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("However, you are lucky to have gotten an early diagnosis. Although there is no cure for Alzheimer's, we have medication ready for you. Please be sure to take it twice, daily", doctor)
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
        dialogue("David, I think you missed a turn", you)
        scene = 1.1111111
    # david's response to the comment
    if scene == 1.1111111 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("No, mom, it's  the next turn", david)
        scene = 1.11111111
    if scene == 1.11111111 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Oh, I'm sorry :(", you)
        scene = 1.2
    # if user says there wasn't a turn
    if scene == 1.111111 and noTurn.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("*David knows the way home.*", you)
        scene = 1.2

    # what happens when the player chooses no
    if scene == 1.01 and noDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        scene = 1.2

    # cactus scene
    if scene == 1.2 and event.type == pygame.MOUSEBUTTONDOWN:
        dialogue("here you go, David.jr, you look a little thirsty.", you)
        scene = 1.21

    if scene == 1.21 and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Did you name a cactus after me?", david)
        scene = 1.22
