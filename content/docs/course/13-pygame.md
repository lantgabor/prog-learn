---
title: "13. PyGame – Játékfejlesztés"
weight: 13
draft: false
---

## Mi az a PyGame?

A PyGame egy Python könyvtár, ami játékok készítésére lett tervezve. A [hivatalos dokumentáció](https://www.pygame.org/docs/) részletes útmutatót és referenciát biztosít. Segít:

- Grafikák megjelenítésében ([pygame.draw dokumentáció](https://www.pygame.org/docs/ref/draw.html))
- Hangok lejátszásában ([pygame.mixer dokumentáció](https://www.pygame.org/docs/ref/mixer.html))
- Felhasználói input kezelésében ([pygame.event dokumentáció](https://www.pygame.org/docs/ref/event.html))

## Koordinátarendszer

A PyGame a képernyő bal felső sarkától számítja a koordinátákat:

- X tengely: balról jobbra növekszik (0-tól ablak szélességéig)
- Y tengely: fentről lefelé növekszik (0-tól ablak magasságáig)
- A (0,0) pont a képernyő bal felső sarka

```
(0,0)     (800,0)
   +----------->  x
   |
   |
   |
   v
   y    (800,600)
```

---

## Első PyGame program

```python
import pygame
pygame.init()

# Ablak létrehozása
ablak = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Első játékom")

# Játék ciklus
fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    ablak.fill((255, 255, 255))  # Fehér háttér
    pygame.display.flip()

pygame.quit()
```

### PyGame ablak és felületek (Surfaces)

A PyGame-ben minden grafikai elem egy **Surface** (felület) objektumon jelenik meg:

#### Ablak létrehozása

```python
ablak = pygame.display.set_mode((szélesség, magasság))
```

- Az ablak maga is egy Surface objektum
- Ez a fő felület, ahova rajzolunk
- A `(800, 600)` azt jelenti, hogy 800 pixel széles és 600 pixel magas lesz

#### Ablak címének beállítása

```python
pygame.display.set_caption("Játék címe")
```

#### Képernyő frissítése

```python
pygame.display.flip()        # Frissíti a teljes képernyőt
pygame.display.update()      # Csak bizonyos részeket frissít
```

A rajzolás csak a `flip()` után válik láthatóvá. Minden frame végén meg kell hívni.

#### Képernyő törlése

```python
ablak.fill((255, 255, 255))  # RGB szín – fehér háttér
```

Általában minden frame elején meghívjuk, hogy "töröljük" az előző frame rajzait.

#### A játék ciklusa (Game Loop)

Minden játéknak van egy fő ciklusa:

1. **Események kezelése** – Billentyűzet, egér, stb.
2. **Játéklogika frissítése** – Pozíciók, ütközések számítása
3. **Képernyő rajzolása** – Grafikák megjelenítése
4. **Képernyő frissítése** – A változások láthatóvá tétele

```python
while fut:
    # 1. Események
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    # 2. Logika
    x += sebesség_x
    y += sebesség_y

    # 3. Rajzolás
    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (255, 0, 0), (x, y), 20)

    # 4. Frissítés
    pygame.display.flip()
```

---

## Rajzolás és az egyszerű alakzatok

A `pygame.draw` modul alapvető rajzolási függvényeket biztosít:

### Téglalap (rect)

`pygame.draw.rect(ablak, szín, (x, y, szélesség, magasság))`

```python
pygame.draw.rect(ablak, (255, 0, 0), (100, 100, 50, 30))
```

<svg width="200" height="150" viewBox="0 0 200 150" style="border: 1px solid #ccc; border-radius: 4px;">
  <rect width="200" height="150" fill="#ffffff"/>
  <rect x="50" y="50" width="100" height="50" fill="#ff0000"/>
</svg>

### Kör (circle)

`pygame.draw.circle(ablak, szín, (x, y), sugár)`

```python
pygame.draw.circle(ablak, (0, 255, 0), (400, 300), 40)
```

<svg width="200" height="150" viewBox="0 0 200 150" style="border: 1px solid #ccc; border-radius: 4px;">
  <rect width="200" height="150" fill="#ffffff"/>
  <circle cx="100" cy="75" r="40" fill="#00ff00"/>
</svg>

### Vonal (line)

`pygame.draw.line(ablak, szín, (x1, y1), (x2, y2), vastagság)`

```python
pygame.draw.line(ablak, (0, 0, 255), (100, 100), (200, 200), 3)
```

<svg width="200" height="150" viewBox="0 0 200 150" style="border: 1px solid #ccc; border-radius: 4px;">
  <rect width="200" height="150" fill="#ffffff"/>
  <line x1="20" y1="20" x2="180" y2="130" stroke="#0000ff" stroke-width="3"/>
</svg>

### Sokszög (polygon)

```python
pontok = [(100, 100), (200, 100), (150, 200)]
pygame.draw.polygon(ablak, (255, 0, 255), pontok)
```

<svg width="200" height="150" viewBox="0 0 200 150" style="border: 1px solid #ccc; border-radius: 4px;">
  <rect width="200" height="150" fill="#ffffff"/>
  <polygon points="50,20 150,20 100,130" fill="#ff00ff"/>
</svg>

### Ellipszis (ellipse)

`pygame.draw.ellipse(ablak, szín, (x, y, szélesség, magasság))`

```python
pygame.draw.ellipse(ablak, (100, 100, 255), (50, 50, 100, 200))
```

### Az összes rajzolási függvény közös paraméterei:

- **ablak**: a rajzolási felület
- **szín**: RGB érték (piros, zöld, kék komponensek 0-255 között)
- **pozíció és méret**: a képernyőn való elhelyezkedés

**Alapszínek:**
- Piros: `(255, 0, 0)`
- Zöld: `(0, 255, 0)`
- Kék: `(0, 0, 255)`
- Fehér: `(255, 255, 255)`
- Fekete: `(0, 0, 0)`

---

## Események kezelése (Events)

A PyGame események rendszere lehetővé teszi, hogy reagáljunk a felhasználói interakciókra.

### Alapvető eseménykezelés

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        fut = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("Szóköz lenyomva!")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print(f"Egér kattintás: {event.pos}")
```

### Gyakori eseménytípusok:

- `pygame.QUIT` – Ablak bezárása
- `pygame.KEYDOWN` – Billentyű lenyomása
- `pygame.KEYUP` – Billentyű felengedése
- `pygame.MOUSEBUTTONDOWN` – Egérgomb lenyomása
- `pygame.MOUSEBUTTONUP` – Egérgomb felengedése
- `pygame.MOUSEMOTION` – Egér mozgatása

### Egér pozíció lekérdezése

```python
x, y = pygame.mouse.get_pos()
print(f"Egér pozíció: ({x}, {y})")
```

### Egérgomb állapot

```python
gombok = pygame.mouse.get_pressed()
if gombok[0]:  # Bal gomb
    print("Bal gomb lenyomva")
if gombok[2]:  # Jobb gomb
    print("Jobb gomb lenyomva")
```

### Körök rajzolása kattintásra

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rajzolj kattintással!")

korok = []  # Körök listája (x, y, szín)

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   # Bal gomb → piros
                korok.append((event.pos[0], event.pos[1], (255, 0, 0)))
            elif event.button == 3: # Jobb gomb → kék
                korok.append((event.pos[0], event.pos[1], (0, 0, 255)))

    ablak.fill((255, 255, 255))
    for x, y, szin in korok:
        pygame.draw.circle(ablak, szin, (x, y), 20)

    pygame.display.flip()

pygame.quit()
```

**Event tulajdonságok:**

- `event.pos` – (x, y) koordináták
- `event.button` – Melyik gomb (1=bal, 2=középső, 3=jobb)
- `event.rel` – Relatív mozgás MOUSEMOTION esetén (dx, dy)

### Rajzolás húzással

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
rajzol = False
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
    if len(pontok) > 1:
        pygame.draw.lines(ablak, (0, 0, 0), False, pontok, 3)

    pygame.display.flip()

pygame.quit()
```

---

## Mozgatás és animáció

### Mi az animáció?

Az animáció valójában egy **illúzió**! Amikor filmeket vagy játékokat nézünk, valójában sok-sok állóképet látunk gyors egymásutánban. Az emberi szem és agy ezeket a képeket összeolvasztja, és folyamatos mozgást érzékel.

**Alapfogalmak:**
- **Frame (képkocka):** Egy egyedi állókép az animációban
- **FPS (Frames Per Second):** Másodpercenként hány képkockát látunk
  - Film: általában 24 FPS
  - Játékok: 30, 60 vagy akár 144 FPS
  - PyGame: tipikusan 60 FPS

### A fizika alapjai: Pozíció, Sebesség, Gyorsulás

#### 1. Pozíció (Position) – \(x\)

A pozíció megmondja, **hol van** az objektum a képernyőn.

```python
x = 100  # 100 pixel a bal széltől
y = 200  # 200 pixel a tetejétől
```

#### 2. Sebesség (Velocity) – \(v\)

A sebesség megmondja, **milyen gyorsan és milyen irányba** mozog az objektum.

$$v = \frac{\Delta x}{\Delta t}$$

```python
sebesség = 5  # 5 pixel mozgás minden frame-ben
x = x + sebesség  # vagy: x += sebesség
```

Ha a sebesség **pozitív**, jobbra mozog. Ha **negatív**, balra mozog.

**Példa számítás:**

Ha egy objektum 100 pixelről 150 pixelre mozog 10 frame alatt:

$$v = \frac{\Delta x}{\Delta t} = \frac{150 - 100}{10} = \frac{50}{10} = 5 \text{ pixel/frame}$$

#### 3. Gyorsulás (Acceleration) – \(a\)

A gyorsulás megmondja, **milyen gyorsan változik a sebesség**.

$$a = \frac{\Delta v}{\Delta t}$$

```python
gyorsulás = 0.5  # Minden frame-ben 0.5 pixel/frame-mel nő a sebesség
sebesség = 0

# Minden frame-ben:
sebesség = sebesség + gyorsulás
x = x + sebesség
```

### Egyenletes mozgás (Konstant sebesség)

$$x_{uj} = x_{regi} + v \cdot \Delta t$$

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 100
y = 300
sebesség_x = 3
sebesség_y = 0

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    x += sebesség_x
    if x > 800:
        x = 0

    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (255, 0, 0), (int(x), int(y)), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

| Frame | x pozíció | Számítás        |
|-------|-----------|-----------------|
| 0     | 100       | Kezdeti érték   |
| 1     | 103       | 100 + 3 = 103   |
| 2     | 106       | 103 + 3 = 106   |
| 3     | 109       | 106 + 3 = 109   |

### Gyorsuló mozgás (gravitáció)

$$v_{uj} = v_{regi} + a \cdot \Delta t$$
$$x_{uj} = x_{regi} + v_{uj} \cdot \Delta t$$

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 400
y = 100
sebesség_y = 0
gyorsulás_y = 0.5  # "Gravitáció" lefelé

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    sebesség_y += gyorsulás_y
    y += sebesség_y

    if y > 600:
        y = 100
        sebesség_y = 0

    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (0, 0, 255), (int(x), int(y)), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### Objektum mozgatása billentyűzettel

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 400
y = 300
sebesség = 5

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= sebesség
    if keys[pygame.K_RIGHT]:
        x += sebesség
    if keys[pygame.K_UP]:
        y -= sebesség
    if keys[pygame.K_DOWN]:
        y += sebesség

    # Határok ellenőrzése
    x = max(20, min(780, x))
    y = max(20, min(580, y))

    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (255, 0, 0), (int(x), int(y)), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### Átlós mozgás – Vektor matematika

Ha egyszerre jobbra ÉS fel nyomsz, az objektum **átlósan** mozog:

$$\text{teljes sebesség} = \sqrt{v_x^2 + v_y^2}$$

Ha \(v_x = 5\) és \(v_y = 5\):

$$v_{teljes} = \sqrt{5^2 + 5^2} = \sqrt{50} \approx 7.07 \text{ pixel/frame}$$

Normalizált (egyforma sebességű) átlós mozgáshoz:

```python
import math

dx = 0
dy = 0
if keys[pygame.K_LEFT]:  dx -= 1
if keys[pygame.K_RIGHT]: dx += 1
if keys[pygame.K_UP]:    dy -= 1
if keys[pygame.K_DOWN]:  dy += 1

if dx != 0 or dy != 0:
    hossz = math.sqrt(dx*dx + dy*dy)
    x += (dx / hossz) * sebesség
    y += (dy / hossz) * sebesség
```

### Delta Time – Frame-független mozgás

**Probléma:** Mi van, ha az FPS változik? Ha 30 FPS-en fut, fele olyan gyorsan mozog, mint 60 FPS-en!

**Megoldás:** Delta time használata

```python
clock = pygame.time.Clock()
sebesség = 200  # pixel/másodperc (nem frame!)

while fut:
    dt = clock.tick(60) / 1000.0  # milliszekundum → másodperc

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += sebesség * dt  # pixel/sec * sec = pixel
```

### Összefoglalás

| Fogalom       | Képlet                           | PyGame kód               |
|---------------|----------------------------------|--------------------------|
| **Pozíció**   | \(x, y\)                           | `x = 100`                |
| **Sebesség**  | \(v = \frac{\Delta x}{\Delta t}\)  | `x += v`                 |
| **Gyorsulás** | \(a = \frac{\Delta v}{\Delta t}\)  | `v += a; x += v`         |
| **Delta Time**| \(\Delta t\)                       | `dt = clock.tick(60) / 1000.0` |

**Alapszabály:** Az animáció nem más, mint apró változások gyors sorozata, amit a szemünk folyamatos mozgásként érzékel!

---

## Sprite-ok használata

### Mi az a Sprite?

A Sprite egy olyan objektum, ami:

- Képet tartalmaz (lehet beépített vagy saját)
- Pozícióval rendelkezik (`rect` tulajdonság)
- Mozgatható (`update()` metódussal)
- Ütközést tud detektálni (`collide` metódusokkal)

### Sprite létrehozása

```python
class Jatekos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
```

### Saját kép használata sprite-hoz

```python
class Jatekos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey((0, 0, 0))  # Átlátszó háttér
        self.rect = self.image.get_rect()
```

### Sprite animálása

```python
class AnimaltJatekos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        for i in range(4):
            img = pygame.image.load(f"player_{i}.png")
            self.frames.append(img)
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.image = self.frames[self.current_frame]
```

### Sprite használata

```python
all_sprites = pygame.sprite.Group()
jatekos = Jatekos()
all_sprites.add(jatekos)

# Játék ciklusban:
all_sprites.update()
all_sprites.draw(ablak)
```

---

## Ütközés detektálás

### Sprite-ok között

```python
class Erme(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

ermek = pygame.sprite.Group()

# Játék ciklusban:
talalatok = pygame.sprite.spritecollide(jatekos, ermek, True)
if talalatok:
    pontszam += len(talalatok)
```

### Téglalap ütközés

```python
teglalap1 = pygame.Rect(x1, y1, w1, h1)
teglalap2 = pygame.Rect(x2, y2, w2, h2)

if teglalap1.colliderect(teglalap2):
    print("Ütközés történt!")
```

---

## Képek és hangok

### Kép betöltése

```python
kep = pygame.image.load("jatekos.png")
kep = pygame.transform.scale(kep, (50, 50))  # Méretezés
```

### Hang lejátszása

```python
pygame.mixer.init()
hang = pygame.mixer.Sound("effect.wav")
hang.play()
```

### Háttérzene

```python
pygame.mixer.music.load("zene.mp3")
pygame.mixer.music.play(-1)  # -1: végtelen ismétlés
```

---

## Gyakorló feladatok

### 1. Mozgó labda

Készíts egy programot, amiben egy labda pattog a képernyőn!

<details>
<summary>Megoldás</summary>

```python
import pygame
pygame.init()

ablak = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 400
y = 300
dx = 5
dy = 5

fut = True
while fut:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

    x += dx
    y += dy

    if x > 780 or x < 20:
        dx *= -1
    if y > 580 or y < 20:
        dy *= -1

    ablak.fill((255, 255, 255))
    pygame.draw.circle(ablak, (255, 0, 0), (x, y), 20)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

</details>

### 2. Érmegyűjtő játék

Készíts egy egyszerű játékot, ahol a játékosnak érméket kell összegyűjtenie!

<details>
<summary>Megoldás</summary>

```python
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
        if keys[pygame.K_LEFT]:  self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_UP]:    self.rect.y -= 5
        if keys[pygame.K_DOWN]:  self.rect.y += 5

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

    talalatok = pygame.sprite.spritecollide(jatekos, ermek, True)
    pontszam += len(talalatok)

    ablak.fill((255, 255, 255))
    all_sprites.draw(ablak)

    font = pygame.font.Font(None, 36)
    szoveg = font.render(f'Pontok: {pontszam}', True, (0, 0, 0))
    ablak.blit(szoveg, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

</details>
