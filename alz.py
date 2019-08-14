# lines may be different since my code didn't have the opening
# line 143
    if scene == 1.01 and yesDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONDOWN:
        screen.fill((0, 0, 0))
        threeMonths = font2.render("Three months later", True, (255, 255, 255))
        screen.blit(threeMonths, ((500 - threeMonths.get_width()) // 2, (600 - threeMonths.get_height()) // 2))
        pygame.display.update()
        scene = 1.001
    if scene == 1.001 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        doctorScene = pygame.image.load('scene 2.png')
        screen.blit(doctorScene, (0,0))
        pygame.display.update()
        dialogue("After analyzing all the tests, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.11

# line 201
    if scene == 1.01 and noDoc.collidepoint(mousePos) and event.type == pygame.MOUSEBUTTONUP:
        dialogue("Ok. Come on. Let's go on our daily walk.", david)
        scene = 1.012
        doctor1 = False
    if scene == 1.012 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        afterWalk = font2.render("After the walk", True, (255, 255, 255))
        screen.blit(afterWalk, ((500 - afterWalk.get_width() // 2), (600 -afterWalk.get_height() // 2)))
        pygame.display.update()

# line 301
    if scene == 1.37 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        sixMonth = font2.render("Six month later", True, (255, 255, 255))
        screen.blit(sixMonth, ((500 - sixMonth.get_width() // 2), (600 - sixMonth.get_height() // 2)))
        pygame.display.update()

# line 378
    scene = 1.05

    # cactus scene
    if scene == 1.05 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        sevenMonth = ("Seven months later", True, (255, 255, 255))
        screen.blit(sevenMonth, ((500 - sevenMonth.get_width() // 2), (600 - sevenMonth.get_height() // 2)))
        pygame.display.update()
        scene = 1.5
        
# line 558
    if scene == 1.65 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        threeMonths = font2.render("Three months later", True, (255, 255, 255))
        screen.blit(threeMonths, ((500 - threeMonths.get_width()) // 2, (600 - threeMonths.get_height()) // 2))
        pygame.display.update()
        scene = 1.065

    if scene == 1.065 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        doctorScene = pygame.image.load('scene 2.png')
        screen.blit(doctorScene, (0,0))
        pygame.display.update()
        dialogue("After analyzing the tests, we can confirm that your mother has Alzheimer’s dementia.", doctor)
        scene = 1.651

# line 614
    if scene == 1.7 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        eightMonth = ("Eight months later", True, (255, 255, 255))
        screen.blit(eightMonth, ((500 - eightMonth.get_width() // 2), (600 - eightMonth.get_height() // 2)))
        pygame.display.update()
        scene = 1.71
