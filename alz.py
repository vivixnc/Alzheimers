import pygame

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

title = font1.render("Alzheimer's", True, (56, 0, 113))
start = font2.render("press space to continue", True, (56, 0, 113))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((0, 0, 0))
    screen.blit(title, ((500 - title.get_width()) // 2, (600 - title.get_height()) // 2))
    screen.blit(start, ((500 - start.get_width()) // 2, (600 - start.get_height()) // 2 + 30))
    pygame.display.flip()
    clock.tick(60)
