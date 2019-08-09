import pygame


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
scene = 0.0
title = font1.render("Alzheimer's", True, (56, 0, 113))
start = font2.render("click anywhere to continue", True, (56, 0, 113))
david = font2.render("David: ", True, (255, 255, 255))
kristyanne = font2.render("Kristy-Anne: ", True, (255, 255, 255))
done = False

def dialogue(line):
    x = 40
    y = 400
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

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    if(scene == 0.0):
        screen.fill((0, 0, 0))
        screen.blit(title, ((500 - title.get_width()) // 2, (600 - title.get_height()) // 2))
        screen.blit(start, ((500 - start.get_width()) // 2, (600 - start.get_height()) // 2 + 30))
        pygame.display.flip()

    if(scene == 0.0 and event.type == pygame.MOUSEBUTTONUP):
        screen.fill((0, 0, 0))
        act1 = font1.render("ACT ONE", True, (255, 255, 255))
        mid = font1.render("MID (2 YEARS)", True, (255, 255, 255))
        screen.blit(act1, ((500 - act1.get_width()) // 2, (600 - act1.get_height()) // 2))
        pygame.draw.line(screen, (255, 255, 255), (150, 320), (350, 320), 1)
        screen.blit(mid, ((500 - mid.get_width()) // 2, (600 - act1.get_height()) // 2 + 50))
        pygame.display.flip()
        scene = 1.0

    if(scene == 1.0 and event.type == pygame.MOUSEBUTTONDOWN):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (20, 0, 56), (0, 350, 500, 700), 0)
        scene = 1.1
        screen.blit(david, (30, 370))
        pygame.display.flip()
        dialogue("Mom, let's go to the doctor to check up on your health. I've noticed your memory has been a little off lately.")

