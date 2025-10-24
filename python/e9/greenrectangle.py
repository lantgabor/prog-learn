import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Green Rectangle with Axes and Label")

center = (200, 200)

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Rectangle (x, y, width, height)
rect = pygame.Rect(150, 150, 100, 50)

# Font
font = pygame.font.SysFont(None, 24)
text = font.render(f"{rect.width} x {rect.height}", True, BLACK)

# Calculate text position (centered inside rectangle)
text_rect = text.get_rect(center=rect.center)

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

    # Draw rectangle
    pygame.draw.rect(screen, GREEN, rect)

    # Draw text
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
