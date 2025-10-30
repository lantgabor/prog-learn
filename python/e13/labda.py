import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 400
y = 300
dx = 5  # x irányú sebesség
dy = 5  # y irányú sebesség

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    # Mozgatás
    x += dx
    y += dy

    # Falakról visszapattanás
    if x > 780 or x < 20:
        dx *= -1
    if y > 580 or y < 20:
        dy *= -1

    # Rajzolás
    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (255, 0, 0),
        (x, y), 20)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
