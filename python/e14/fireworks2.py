import math
import random

import pygame


class Particle:
    """
    A small particle produced by a firework explosion.
    Has position, velocity, color and life. Leaves a short trail.
    """

    def __init__(self, x, y, vx, vy, color, lifespan=80):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.base_color = color  # (r,g,b)
        self.lifespan = lifespan
        self.age = 0
        self.trail = []  # list of previous positions for trail
        self.max_trail = 8

    def update(self, gravity=0.15):
        # store trail
        self.trail.insert(0, (self.x, self.y))
        if len(self.trail) > self.max_trail:
            self.trail.pop()

        # physics
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy

        self.age += 1

    @property
    def alive(self):
        return self.age < self.lifespan

    def draw(self, surface):
        # fade factor 1..0
        factor = max(0.0, 1.0 - (self.age / float(self.lifespan)))
        # scale color
        r = int(self.base_color[0] * factor)
        g = int(self.base_color[1] * factor)
        b = int(self.base_color[2] * factor)
        color = (r, g, b)

        # draw trail (older = fainter, smaller)
        for i, (tx, ty) in enumerate(self.trail):
            t_factor = factor * (1.0 - (i / max(1, len(self.trail))))
            tr = int(self.base_color[0] * t_factor)
            tg = int(self.base_color[1] * t_factor)
            tb = int(self.base_color[2] * t_factor)
            pygame.draw.circle(
                surface, (tr, tg, tb), (int(tx), int(ty)), max(1, 3 - i // 3)
            )

        # draw particle
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 3)


class Firework:
    """
    The main firework (rocket) that shoots up, leaves a trail, and then explodes
    into several `Particle`s when it reaches its specified explosion_height.
    """

    def __init__(self, x, y, color, explosion_height, angle_jitter=0.4):
        self.x = x
        self.y = y
        # initial upward velocity with small random x component
        angle = -math.pi / 2 + random.uniform(-angle_jitter, angle_jitter)
        speed = random.uniform(6.5, 9.0)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.color = color  # (r,g,b)
        self.explosion_height = explosion_height
        self.trail = []
        self.max_trail = 12
        self.exploded = False
        self.particles = []  # holds Particle objects after explosion
        self.age = 0

    def update(self, gravity=0.15):
        self.age += 1
        if not self.exploded:
            # rocket physics
            self.vy += gravity
            self.x += self.vx
            self.y += self.vy

            # update trail
            self.trail.insert(0, (self.x, self.y))
            if len(self.trail) > self.max_trail:
                self.trail.pop()

            # check for explosion condition (y <= explosion_height or vy>0 after peak)
            if self.y <= self.explosion_height or self.vy > 0:
                self.explode()
        else:
            # update child particles
            for p in self.particles:
                p.update(gravity)
            # remove dead particles
            self.particles = [p for p in self.particles if p.alive]

    def explode(self):
        if self.exploded:
            return
        self.exploded = True

        # create 8-directional particles (N, NE, E, SE, S, SW, W, NW)
        directions = []
        for i in range(8):
            ang = -math.pi / 2 + i * (math.pi / 4)  # start at North and go clockwise
            directions.append(ang)

        speed = random.uniform(2.5, 5.5)
        for ang in directions:
            vx = math.cos(ang) * speed * random.uniform(0.7, 1.3)
            vy = math.sin(ang) * speed * random.uniform(0.7, 1.3)
            # give each small particle a small random lifespan
            lifespan = random.randint(50, 120)
            p = Particle(self.x, self.y, vx, vy, self.color, lifespan)
            # seed each particle trail with a few points so there's an immediate trail
            p.trail = [(self.x - vx * i * 0.2, self.y - vy * i * 0.2) for i in range(3)]
            self.particles.append(p)

    @property
    def alive(self):
        # alive if not exploded or still has particles
        if not self.exploded:
            return True
        return len(self.particles) > 0

    def draw(self, surface):
        if not self.exploded:
            # draw trail
            for i, (tx, ty) in enumerate(self.trail):
                t_factor = 1.0 - (i / max(1, len(self.trail)))
                tr = int(self.color[0] * t_factor)
                tg = int(self.color[1] * t_factor)
                tb = int(self.color[2] * t_factor)
                pygame.draw.circle(
                    surface, (tr, tg, tb), (int(tx), int(ty)), max(1, 4 - i // 3)
                )
            # draw rocket
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 4)
        else:
            # draw particles
            for p in self.particles:
                p.draw(surface)


# lowercase alias for compatibility with user's requested class name
firework = Firework


def random_bright_color():
    # pick a random hue and return an RGB triple that's bright/saturated
    c = pygame.Color(0)
    h = random.randint(0, 359)
    c.hsva = (h, 100, 100, 100)
    return (c.r, c.g, c.b)


def main():
    pygame.init()

    width = 600
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    # Spawn 10 fireworks at the beginning of the first frame
    fireworks = []
    for _ in range(10):
        x = random.randint(50, width - 50)
        y = height - 10  # start near bottom
        color = random_bright_color()
        # explosion height somewhere in upper half
        explosion_height = random.randint(60, height // 2)
        fw = Firework(x, y, color, explosion_height)
        fireworks.append(fw)

    running = True
    frame = 0
    gravity = 0.16

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Background
        # slightly alpha darken background to create lingering trails effect
        screen.fill((0, 0, 0))

        # Update fireworks
        for fw in fireworks:
            fw.update(gravity=gravity)
        # remove finished fireworks
        fireworks = [fw for fw in fireworks if fw.alive]

        # Draw fireworks
        for fw in fireworks:
            fw.draw(screen)

        # If everything finished, spawn a new batch after a short pause
        if not fireworks:
            # spawn a new bunch to keep the show alive
            for _ in range(10):
                x = random.randint(50, width - 50)
                y = height - 10
                color = random_bright_color()
                explosion_height = random.randint(60, height // 2)
                fw = Firework(x, y, color, explosion_height)
                fireworks.append(fw)

        pygame.display.flip()
        clock.tick(60)
        frame += 1

    pygame.quit()


if __name__ == "__main__":
    main()
