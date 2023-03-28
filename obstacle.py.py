import pygame
import random
import winsound

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the game window
pygame.display.set_caption("My Game")

# Set the font for the score
score_font = pygame.font.SysFont('comicsansms', 30)

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the player properties
player_size = 50
player_x = 225
player_y = 450

# Set the obstacle properties
obstacle_size = 50
obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_size)
obstacle_y = -50
obstacle_speed = 1

# Set the score
score = 0

# Set the game loop
game_loop = True
while game_loop:

# Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

# Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_size:
        player_x += 5

# Move the obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > WINDOW_HEIGHT:
        obstacle_x = random.randint(0, WINDOW_WIDTH - obstacle_size)
        obstacle_y = -50
        score += 1
        obstacle_speed += 1
        winsound.PlaySound("score.wav",winsound.SND_ASYNC)

# Collision
    if obstacle_y + obstacle_size > player_y:
        if obstacle_x >= player_x and obstacle_x < player_x + player_size or player_x >= obstacle_x and player_x < obstacle_x + obstacle_size:
            game_loop = False

# Draw the background
    window.fill(WHITE)

# Draw the player
    pygame.draw.rect(window, BLACK, (player_x, player_y, player_size, player_size))

# Draw the obstacle
    pygame.draw.rect(window, RED, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))

# Draw the score
    score_text = score_font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

# Update the window
    pygame.display.update()

# Add delay to slow down the game
    pygame.time.delay(3)

# Quit Pygame
pygame.quit()
