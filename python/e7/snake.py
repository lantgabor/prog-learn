# snake_pygame.py
# Simplest Snake with pygame

import pygame, sys, random

# Setup
pygame.init()
CELL = 20
WIDTH, HEIGHT = 20, 20  # 20x20 grid
SCREEN = pygame.display.set_mode((WIDTH*CELL, HEIGHT*CELL))
CLOCK = pygame.time.Clock()

def draw_rect(color, pos):
    r = pygame.Rect(pos[0]*CELL, pos[1]*CELL, CELL, CELL)
    pygame.draw.rect(SCREEN, color, r)

def main():
    snake = [[WIDTH//2, HEIGHT//2]]
    direction = (1, 0)  # start moving right
    food = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
    score = 0

    while True:
        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT: pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP: direction = (0,-1)
                elif e.key == pygame.K_DOWN: direction = (0,1)
                elif e.key == pygame.K_LEFT: direction = (-1,0)
                elif e.key == pygame.K_RIGHT: direction = (1,0)

        # Move snake
        head = [snake[0][0]+direction[0], snake[0][1]+direction[1]]

        # Check collision
        if (head in snake or head[0]<0 or head[0]>=WIDTH or head[1]<0 or head[1]>=HEIGHT):
            print("Game Over! Score:", score)
            pygame.quit(); sys.exit()

        snake.insert(0, head)

        # Eat food
        if head == food:
            score += 1
            food = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
        else:
            snake.pop()

        # Draw
        SCREEN.fill((0,0,0))
        for s in snake: draw_rect((0,255,0), s)
        draw_rect((255,0,0), food)
        pygame.display.flip()
        CLOCK.tick(10)  # speed

if __name__ == "__main__":
    main()
