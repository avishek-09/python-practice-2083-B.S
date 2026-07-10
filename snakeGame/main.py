import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("cosmicsansms", 16) 
x = 20 
y = 20 
speed = 5
velocity_x = 0
velocity_y = 0
width = 25
height = 25
fps = 30
food_x = randint(40,750)
food_y = randint(50,450)
food_h = 10
food_w = 10
score = 0
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

    pygame.draw.circle(screen, (255,200,0), [food_x,food_y], 8)

    text = font.render(f"Score: {score}", True, (0, 128, 0))

    screen.blit(text, [750,10])

    pygame.display.update()

    pygame.time.Clock().tick(fps)

pygame.quit()