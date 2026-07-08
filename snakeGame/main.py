import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                playing = False