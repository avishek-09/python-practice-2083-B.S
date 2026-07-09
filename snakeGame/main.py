import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
x = 20 
y = 20 
speed = 5
velocity_x = 0
velocity_y = 0
width = 50
height = 25

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                playing = False
            elif event.key == pygame.K_RIGHT:
                velocity_x = speed
                velocity_y = 0
            elif event.key == pygame.K_LEFT:
                velocity_x = -speed
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = - speed
                velocity_x = 0
            elif event.key == pygame.K_DOWN :
                velocity_y = speed
                velocity_x = 0


    # x = x + 0.1
    x += velocity_x
    y += velocity_y

    screen.fill((255,255,255))

    pygame.draw.rect(screen, (0,255,100), [x,y,width,height])

    pygame.display.update()

    pygame.time.Clock().tick(80)

pygame.quit()