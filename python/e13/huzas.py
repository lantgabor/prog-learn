import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
rajzol = False  # Éppen rajzolunk-e

pontok = []

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            rajzol = True
        elif event.type == pygame.MOUSEBUTTONUP:
            rajzol = False
        elif event.type == pygame.MOUSEMOTION:
            if rajzol:
                pontok.append(event.pos)

    ablak.fill((255, 255, 255))

    # Vonalak rajzolása a pontok között
    if len(pontok) > 1:
        pygame.draw.lines(ablak, (0, 0, 0), False, pontok, 3)

    pygame.display.flip()

pygame.quit()
