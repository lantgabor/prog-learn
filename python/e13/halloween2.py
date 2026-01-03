import pygame


class pont:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def tuple(self):
        return (self.X, self.Y)

    def tuple2(self):
        return (self.X + 50, self.Y)

    def tuple3(self):
        return (self.X + 100, self.Y)


class negyzet:
    def __init__(self, szin, A: pont, W, H):
        self.szin = szin
        self.A = A
        self.W = W
        self.H = H

    def rajzol(self, screen):
        pygame.draw.rect(
            screen, self.szin, pygame.Rect(self.A.tuple(), (self.W, self.H))
        )


class kor:
    def __init__(self, szin, K: pont, r):
        self.szin = szin
        self.K = K
        self.r = r

    def rajzol(self, screen):
        pygame.draw.circle(screen, self.szin, self.K.tuple(), self.r)


class haromszog:
    def __init__(self, szin, A: pont, B: pont, C: pont):
        self.szin = szin
        self.A = A
        self.B = B
        self.C = C

    def rajzol(self, screen):
        pontok = [self.A.tuple(), self.B.tuple(), self.C.tuple()]
        pygame.draw.polygon(screen, self.szin, pontok)


class tok:
    def __init__(self, szin, x, y):
        self.szin = szin
        self.x = x
        self.y = y
        self.R = 88

    def rajzol(self, screen):
        kor1 = kor("Orange", pont(self.x, self.y), 88)
        kor2 = kor("Orange", pont(self.x + 50, self.y), 88)
        kor3 = kor("Orange", pont(self.x + 100, self.y), 88)

        kor1.rajzol(screen)
        kor2.rajzol(screen)
        kor3.rajzol(screen)

        # szemek
        # haromszog3 = haromszog("Black", pont(350, 270), pont(380, 245), pont(410, 270))
        # haromszog3.rajzol(screen)

        # haromszog4 = haromszog("Black", pont(450, 270), pont(480, 245), pont(510, 270))
        # haromszog4.rajzol(screen)

        # # tok szara
        # haromszog5 = haromszog("Green", pont(425, 172), pont(435, 192), pont(450, 212))
        # haromszog5.rajzol(screen)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

negyzet1 = negyzet("Yellow", pont(111, 222), 51, 51)

# tok eleje


korok = []
negyzetek = []
tokok = []
alakzat_tipus = 1

# hatter
screen.fill("Black")

# kezdodik a  rajzolas
negyzet1.rajzol(screen)

# tok eleje

# tok vege


for i in range(5):
    haromszog1 = haromszog(
        "Black",
        pont(350 + i * 30, 325),
        pont(380 + i * 30, 350),
        pont(410 + i * 30, 325),
    )
    haromszog2 = haromszog(
        "Black",
        pont(350 + i * 30, 325),
        pont(380 + i * 30, 300),
        pont(410 + i * 30, 325),
    )
    haromszog1.rajzol(screen)
    haromszog2.rajzol(screen)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                alakzat_tipus = 1
            elif event.key == pygame.K_2:
                alakzat_tipus = 2
            elif event.key == pygame.K_3:
                alakzat_tipus = 3

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if alakzat_tipus == 1:
                korok.append(kor("Orange", pont(x, y), 55))
            elif alakzat_tipus == 2:
                negyzetek.append(negyzet("Red", pont(x, y), 45, 45))
            elif alakzat_tipus == 3:
                tokok.append(tok("Orange", x, y))
    if korok:
        for k in korok:
            k.rajzol(screen)
    if negyzetek:
        for n in negyzetek:
            n.rajzol(screen)
    if tokok:
        for t in tokok:
            t.rajzol(screen)
    pygame.display.flip()
pygame.quit()
