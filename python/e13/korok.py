import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rajzolj kattintással!")

# Körök listája (x, y, szín)
korok = []

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Bal gomb kattintás
            if event.button == 1:
                x, y = event.pos
                szin = (255, 0, 0)  # Piros
                korok.append((x, y, szin))
            # Jobb gomb kattintás
            elif event.button == 3:
                x, y = event.pos
                szin = (0, 0, 255)  # Kék
                korok.append((x, y, szin))

    # Képernyő törlése
    ablak.fill((255, 255, 255))

    # Összes kör rajzolása
    for x, y, szin in korok:
        pygame.draw.circle(ablak, szin, (x, y), 20)

    pygame.display.flip()

pygame.quit()
