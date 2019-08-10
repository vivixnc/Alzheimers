import pygame
import sys
# music link: https://www.soundjay.com/communication-sounds.html
# its the second one:)

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

# instantiating names for dialogue
david = font2.render("David: ", True, (255, 255, 255))
kristyanne = font2.render("Kristy-Anne: ", True, (255, 255, 255))

# making yes and no buttons for act one scene 1
yes = pygame.Rect(75, 550, 150, 80)
no = pygame.Rect(275, 550, 150, 80)

done = False

def dialogue(line):
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.init()
    pygame.mixer.music.load("computer-keyboard-2.wav")
    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play(-1)
    x = 40
    y = 450
    i = 0
    for i in range (len(line)):
        if(x >= 450 and line[i] == " "):
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

        # drawing textbox
        pygame.draw.rect(screen, (20, 0, 56), (0, 400, 500, 700), 0)
        screen.blit(david, (30, 420))
        pygame.display.update()

        # printing text
        dialogue("Mom, let's go to the doctor to check up on your health. I've noticed your memory has been a little off lately......")

        # drawing yes and no buttons (box only)
        pygame.draw.rect(screen, [0, 0, 0], yes)
        pygame.draw.rect(screen, [0, 0, 0], no)

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
    if scene == 1.01 and yes.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((255, 0, 0))
        pygame.display.update()
        scene = 1.1

    # what happens when the player chooses no
    if scene == 1.01 and no.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        screen.fill((0, 255, 0))
        pygame.display.update()
        scene = 1.1
