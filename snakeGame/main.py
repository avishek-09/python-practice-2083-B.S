## import and initailaize
import pygame
from random import randint
pygame.init()


## Display setting for the game
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("comicsansms", 15) 
mid_font = pygame.font.SysFont("comicsansms", 40)
larger_font = pygame.font.SysFont("comicsansms", 80)


## pause the game
def handle_pause():
    pause = True
    while pause: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    

## variables to define position, speed, fps and score
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


## actual logic behind the whole game working process
playing = True
game_over = False
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                playing = False
            elif event.key == pygame.K_p:
                handle_pause()
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
            

        text = font.render(f"Score: {score}", True, (0, 128, 0))
        screen.blit(text, [720,10])

    if not game_over: 
        ## logic behind snake moving
        x += velocity_x
        y += velocity_y

        screen.fill((0,0,0))

        pygame.draw.rect(screen, (0,255,100), [x,y,width,height])

        pygame.draw.circle(screen, (255,200,0), [food_x,food_y], 8)

        snake_rect = pygame.Rect(x, y, width, height)
        food_circle = pygame.Rect(food_x, food_y, food_w, food_h)

        if snake_rect.colliderect(food_circle):
            score += 10 
            fps += 3
            food_x = randint(40,750)
            food_y = randint(50,450)

        

        if x<5 or x>770 or y<5 or y>470:
            game_over = True
            over = larger_font.render("Game Over", True, (255, 0, 0))
            screen.blit(over, [200,160])
            text = mid_font.render(f"Score: {score}", True, (0, 128, 0))
            screen.blit(text, [310,270])

            

    text = font.render(f"Score: {score}", True, (0, 128, 0))
    screen.blit(text, [725,10])

    pygame.display.update()

    pygame.time.Clock().tick(fps)

