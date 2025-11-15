import pygame
pygame.init()

# Ablak létrehozása
ablak = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Első játékom")

# Játék ciklus
fut = True
while fut:
    # Események kezelése
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    # Képernyő törlése
    ablak.fill((255, 255, 255))  # Fehér háttér

    pygame.draw.rect(ablak, (255, 0, 0),
        (100, 100, 50, 30))

    pygame.draw.circle(ablak, (0, 255, 0),
        (400, 300), 40)

    pontok = [(100, 100), (200, 100), (150, 200)]
    pygame.draw.polygon(ablak, (255, 0, 255), pontok)

    pygame.draw.ellipse(ablak, (100, 100, 255), (50, 50, 100, 200))

    pygame.draw.line(ablak, (0, 0, 255), (100, 100), (200, 200), 3)

    # Frissítés
    pygame.display.flip()

# Kilépés
pygame.quit()
