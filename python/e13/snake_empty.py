import random

import pygame


def main():
    pygame.init()

    width = 600
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    # Jaték kezdete előtt...

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # fel
                    pass
                elif event.key == pygame.K_DOWN:
                    # le
                    pass
                elif event.key == pygame.K_RIGHT:
                    # jobbra
                    pass
                elif event.key == pygame.K_LEFT:
                    # balra
                    pass

        # Háttér
        screen.fill((51, 51, 51))

        # Játék futás közben ELEJE

        # Jéték futás közben VÉGE
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
