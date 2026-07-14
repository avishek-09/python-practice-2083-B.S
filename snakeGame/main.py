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
restart_image = pygame.image.load("assest/restart.png")
restart_image = pygame.transform.scale(restart_image, (50,50))
restart_rectangle = pygame.Rect(370,350,50,50)
 


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
fps = 30
def game_init():
    global x,y,speed, velocity_x, velocity_y, width, height, food_x, food_y, food_h, food_w, score, fps, snake_list, snake_length
    fps = 30
    x = 20 
    y = 20 
    speed = 5
    velocity_x = 0
    velocity_y = 0
    width = 25
    height = 25
    food_x = randint(40,750)
    food_y = randint(50,450)
    food_h = 10
    food_w = 10
    score = 0
    snake_list = []
    snake_length = 1

game_init()
## actual logic behind the whole game working process
playing = True
game_over = False
while playing:
    pygame.mixer.Sound("assest/music.mp3").play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                playing = False
            elif event.key == pygame.K_p:
                handle_pause()
            elif event.key == pygame.K_RIGHT:
                pygame.mixer.Sound("assest/move.mp3").play()
                velocity_x = speed
                velocity_y = 0
            elif event.key == pygame.K_LEFT:
                pygame.mixer.Sound("assest/move.mp3").play()
                velocity_x = -speed
                velocity_y = 0
            elif event.key == pygame.K_UP:
                pygame.mixer.Sound("assest/move.mp3").play()
                velocity_y = - speed
                velocity_x = 0
            elif event.key == pygame.K_DOWN :
                pygame.mixer.Sound("assest/move.mp3").play()
                velocity_y = speed
                velocity_x = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if restart_rectangle.collidepoint(event.pos):
                    game_over = False
                    game_init()
            
    if not game_over: 
        ## logic behind snake moving
        x += velocity_x
        y += velocity_y
        head = [x, y]
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        ## logic to refresh the display
        screen.fill((0,0,0))

        ## config for the snake
        for body in snake_list:
            pygame.draw.rect(screen, (0,255,100), [body[0],body[1],width,height])

        ## config for the snake food
        pygame.draw.circle(screen, (255,200,0), [food_x,food_y], 8)

        snake_rect = pygame.Rect(x, y, width, height)
        food_circle = pygame.Rect(food_x, food_y, food_w, food_h)

        ## logic behind eating the food
        if snake_rect.colliderect(food_circle):
            pygame.mixer.Sound("assest/food.mp3").play()
            score += 10 
            fps += 3
            food_x = randint(40,750)
            food_y = randint(50,450)
            snake_length += 1

        
        ## logic behind the game over
        if x<5 or x>770 or y<5 or y>470:
            game_over = True
            pygame.mixer.Sound("assest/gameover.mp3").play()
            over = larger_font.render("Game Over", True, (255, 0, 0))
            screen.blit(over, [200,160])
            text = mid_font.render(f"Score: {score}", True, (0, 128, 0))
            screen.blit(text, [310,270])
            screen.blit(restart_image, [370,350])

    text = font.render(f"Score: {score}", True, (0, 128, 0))
    screen.blit(text, [725,10])

    pygame.display.update()

    pygame.time.Clock().tick(fps)

