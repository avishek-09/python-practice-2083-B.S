import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
x = 20 
y = 20 
speed = 5

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                playing = False
            elif event.key == pygame.K_RIGHT:
                x = x + speed
            elif event.key == pygame.K_LEFT:
                x = x - speed
            elif event.key == pygame.K_UP:
                y = y - speed
            elif event.key == pygame.K_DOWN :
                y = y + speed


    # x = x + 0.1

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (255,0,0), [x,y,100,100])

    pygame.display.update()

    pygame.time.Clock().tick(1080)

pygame.quit()