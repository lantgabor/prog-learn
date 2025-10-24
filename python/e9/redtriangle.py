import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Red Triangle with Axes")

# Define points (x, y)
points = [(200, 65), (100, 300), (300, 300)]
center = (0, 0)

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw axes
    pygame.draw.line(screen, BLACK, (0, center[1]), (400, center[1]), 2)  # X-axis
    pygame.draw.line(screen, BLACK, (center[0], 0), (center[0], 400), 2)  # Y-axis

    # Draw triangle
    pygame.draw.polygon(screen, RED, points)

    pygame.display.flip()

pygame.quit()
