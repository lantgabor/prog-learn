import pygame
import random

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.total = 0
        self.tail = []

    def eat(self, pos):
        d = ((self.x - pos[0])**2 + (self.y - pos[1])**2)**0.5
        if d < 1:
            self.total += 1
            return True
        else:
            return False

    def dir(self, x, y):
        self.xspeed = x
        self.yspeed = y

    def death(self):
        for pos in self.tail:
            d = ((self.x - pos[0])**2 + (self.y - pos[1])**2)**0.5
            if d < 1:
                print('starting over')
                self.total = 0
                self.tail = []
                return True
        return False

    def update(self, scl, width, height):
        for i in range(len(self.tail) - 1):
            self.tail[i] = self.tail[i + 1]

        if self.total >= 1:
            if len(self.tail) < self.total:
                self.tail.append((self.x, self.y))
            else:
                self.tail[self.total - 1] = (self.x, self.y)

        self.x = self.x + self.xspeed * scl
        self.y = self.y + self.yspeed * scl

        self.x = max(0, min(self.x, width - scl))
        self.y = max(0, min(self.y, height - scl))

    def show(self, screen, scl):
        for i in range(len(self.tail)):
            pygame.draw.rect(screen, (255, 255, 255), (self.tail[i][0], self.tail[i][1], scl, scl))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, scl, scl))


def pick_location(width, height, scl):
    cols = width // scl
    rows = height // scl
    food_x = random.randint(0, cols - 1) * scl
    food_y = random.randint(0, rows - 1) * scl
    return (food_x, food_y)


def main():
    pygame.init()

    width = 600
    height = 600
    scl = 20

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
                elif event.key == pygame.K_DOWN:
                   # le
                elif event.key == pygame.K_RIGHT:
                   # jobbra
                elif event.key == pygame.K_LEFT:
                   # balra

        # Háttér
        screen.fill((51, 51, 51))

        # Játék futás közben ELEJE


        # Jéték futás közben VÉGE
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
