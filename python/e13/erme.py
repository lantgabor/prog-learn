import pygame
import random

class Jatekos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

class Erme(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(780)
        self.rect.y = random.randrange(580)

pygame.init()
ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
ermek = pygame.sprite.Group()
jatekos = Jatekos()
all_sprites.add(jatekos)

for i in range(10):
    erme = Erme()
    all_sprites.add(erme)
    ermek.add(erme)

pontszam = 0
fut = True

while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    all_sprites.update()

    talalatok = pygame.sprite.spritecollide(
        jatekos, ermek, True)
    pontszam += len(talalatok)

    ablak.fill((255, 255, 255))
    all_sprites.draw(ablak)

    # Pontszám kiírása
    font = pygame.font.Font(None, 36)
    szoveg = font.render(f'Pontok: {pontszam}',
        True, (0, 0, 0))
    ablak.blit(szoveg, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
