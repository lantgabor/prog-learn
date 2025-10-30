import os
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Halloween Jumper")

# Colors
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Player properties
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# Load player sprite
import os

# Get the directory where the game script is located
game_dir = os.path.dirname(os.path.abspath(__file__))
sprite_path = os.path.join(game_dir, "Png_animation", "Ghost1.png")

try:
    print(f"Attempting to load sprite from: {sprite_path}")
    player_image = pygame.image.load(sprite_path)
    print("Sprite loaded successfully!")
    # player_image = pygame.transform.scale(
    #     player_image, (PLAYER_WIDTH, PLAYER_HEIGHT)
    # )
except (pygame.error, FileNotFoundError) as e:
    player_image = None
    print(f"Could not load ghost sprite: {e}")
player_x = 50
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5
player_jump = -15
player_velocity = 0
GRAVITY = 0.8

# Ground platform
GROUND = pygame.Rect(0, WINDOW_HEIGHT - 10, WINDOW_WIDTH, 10)

# Game loop
clock = pygame.time.Clock()
running = True
player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_velocity == 0:
                player_velocity = player_jump

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Apply gravity
    player_velocity += GRAVITY
    player_rect.y += player_velocity

    # Ground collision
    if player_rect.colliderect(GROUND):
        player_rect.bottom = GROUND.top
        player_velocity = 0

    # Keep player in bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WINDOW_WIDTH:
        player_rect.right = WINDOW_WIDTH

    # Clear screen
    screen.fill(BLACK)

    # Draw ground
    pygame.draw.rect(screen, ORANGE, GROUND)

    # Draw player (ghost)
    if player_image:
        print(f"Drawing sprite at position: {player_rect.x}, {player_rect.y}")
        screen.blit(player_image, (player_rect.x, player_rect.y))
    else:
        print("Fallback: Drawing rectangle")
        pygame.draw.rect(screen, ORANGE, player_rect)

    # Update display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

pygame.quit()
