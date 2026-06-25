---
title: "1. Bevezetés a programozásba"
weight: 1
draft: false
---

## Mi az a "programozás"?

A programozás az, amikor megmondjuk egy számítógépnek, hogy mit csináljon.
Úgy adunk neki **utasításokat**, hogy azokat **pontosan megérti** és **végrehajtja**.

![gandalf](/img/gandalf.jpg)

## Mit lehet vele csinálni?

### 1. Játékokat készíteni

![bg3](/img/bg3.jpg)

### 2. Weboldalakat fejleszteni

![facebook](/img/facebook.png)

### 3. Robotokat irányítani

![apollo15](/img/apollo15.jpg)

### 4. Zenét, videókat szerkeszteni

![sphere](/img/sphere.png)

### 5. Mesterséges intelligenciát tanítani

### 6. Automatizálni unalmas feladatokat

---

## Hol használjuk, hol találkozol vele?

Gyakorlatilag mindenhol:

- Telefonokban
- Autókban
- Laptopokon
- TV-ben
- Okosórákban
- Hűtőben, porszívóban, sőt, még hajvasalóban is!

**Bármi, amiben elektronika van, és amire valamilyen utasítást lehet adni, az valójában egy számítógép.** Nem csak az, amin Windows fut!

---

## Mit csinálnak a számítógépek?

Feladatokat oldanak meg. De hogyan?

Úgy, ahogy mi emberek is: **lépésről lépésre, utasításokat követve.**

![step](/img/step.jpg)

## Mit nevezünk utasításnak?

Olyan **parancs**, amit a gép **ért** és **végrehajt**.

Például:

- Rányomsz egy gombra a telefonon → megnyílik egy app.
- Beírsz valamit a Google-be → kiadja a találatokat.

Ez mind-mind egy-egy sor utasítás a háttérben.

![instuction](/img/instuction.png)

## Mi történik ilyenkor?

Nem kell pontosan tudni, mi zajlik belül, de annyi biztos, hogy a számítógép olvassa az általad adott utasításokat, végrehajtja őket, és visszaad valamilyen eredményt.

![work](/img/work.png)

---

## Miért jó programozni?

Mert amit kigondolsz, azt meg tudod valósítani.

Olyan, mint:

- Festeni egy képet.
- Megépíteni valamit LEGO-ból.
- Megírni egy dalt.

![computer_problems](/img/computer_problems.png)

Csak itt a végeredmény egy app, egy játék, egy robot vagy valami más menő dolog.

---

## Mit fogunk csinálni?

- Csinálhatunk egyszerű játékot (Flappy Bird?)
- Megnézzük, hogyan működnek a nagyobb játékok (pl. Genshin Impact – persze nem fogjuk megírni, de megérthetjük az alapokat)
- Készítünk mini alkalmazásokat

![mario](/img/mario.jpg)

---

## Mit fogunk tanulni?

### Python ![pythonlogo](/img/pythonlogo.png)

- Mi az a Python? Egy szuper népszerű programozási nyelv, amit kezdők és profik is szeretnek.
- Mi az, hogy programozási nyelv? Olyan, mint egy beszélt nyelv, csak itt az ember és a gép beszélget egymással.

![python2](/img/python2.png)

## Python telepítése

Megmutatom lépésről lépésre, hogyan kell Windowson [telepíteni](https://www.python.org/), hogy tudjunk kódolni.

---

## Hogyan kapcsolódik a matematika a programozáshoz?

Sokszor ugyanúgy gondolkodunk, mint a matekban: **megoldunk feladatokat, szabályokat követünk.**

A tudást alapvetően kétféleképpen csoportosítjuk:

| Deklaratív | Imperatív |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **"Mi az, ami igaz?"** – Állításokat teszünk | **"Hogyan kell csinálni?"** – Lépéseket adunk meg |
| Például: \(x\) gyöke az a \(y\), amire \(y^2 = x\) és \(y \geq 0\) | Tippelj egy \(y'\) értéket, javítsd így: \((y'+x/y')/2\), amíg jó nem lesz. |
| Megmondjuk, milyenek a helyes megoldások, a gép kitalálja a módszert | Pontosan leírjuk, milyen lépéseket hajtson végre a gép |
| Például: "Egy olyan számot keresünk, amelynek a négyzete 9." | "Vedd a 9-et, próbálj ki számokat, nézd meg, melyik négyzete 9" |

## Algoritmusok

Az algoritmus = recept.

![choccoveredcherries](/img/choccoveredcherries.jpg)

Olyan lépések sorozata, amik elvezetnek egy megoldáshoz.

Egy jó algoritmus:

- **Pontos** (nincs benne félreérthető lépés)
- **Véges** (nem tart örökké)
- **A megengedett utasításokból áll** (amit a gép ért)

---

## Példa algoritmus

**Mit tegyek, ha nem kapcsol fel a lámpa?**

- Nézd meg, be van-e dugva.
- Nézd meg, jó-e az égő.
- Cseréld ki a lámpát.

### Hogyan írunk le egy algoritmust?

1. **Beszélt nyelven** (pszeudokód)
2. **Folyamatábrával**

Ez egy folyamatábra formájában így nézhet ki:

![Folyamatábra](/img/flowchart.png)

## Pszeudokód példa

Egy szám számjegyeinek összege.

```
Be: szam
osszeg = 0

Amíg szam > 0:
    osszeg += szam % 10
    szam = szam / 10

Ki: "A szám számjegyeinek összege: " + osszeg
```

## A programkód

Ez már az, amit a gép valóban ért.

- A számítógép ezt érti. Programozási nyelven írjuk.
- A nyelv elemei, **szótár**
- **Szintaxis**, nyelvtani szabályok.

```python
# legnagyobb közös osztó
a = int(input("a? "))
b = int(input("b? "))

while b != 0:
    t = b
    b = a % b
    a = t

print("lnko =", a)
```

---

## Hello world

Minden programozási nyelven elérhető a `Hello world!`

```python
print("Hello Sissy!")
```

```
Hello Sissy!
```

Mi is történik itt?

- `print()` Kiírunk valamit
- `"szöveg"` Karakterek, másnéven `string`, szöveges elem
- `()` zárójel a függvény paraméterei

**Számológép**

```python
print("Megoldás: ", 7 + 3)
```

```
Megoldás: 10
```

---

## További nyelvi elemek

### Érték adás

```python
változó = "érték"
```

A `változó` most tartalmazza az `"érték"` szöveget.

### 1. Aritmetikai operátorok

| Operátor | Leírás            | Példa    |
| -------- | ----------------- | -------- |
| `+`      | Összeadás         | `a + b`  |
| `-`      | Kivonás           | `a - b`  |
| `*`      | Szorzás           | `a * b`  |
| `/`      | Osztás            | `a / b`  |
| `//`     | Egész osztás      | `a // b` |
| `%`      | Maradék (modulus) | `a % b`  |
| `**`     | Hatványozás       | `a ** b` |

### 2. Összehasonlító operátorok

| Operátor | Leírás               | Példa    |
| -------- | -------------------- | -------- |
| `==`     | Egyenlő              | `a == b` |
| `!=`     | Nem egyenlő          | `a != b` |
| `>`      | Nagyobb, mint        | `a > b`  |
| `<`      | Kisebb, mint         | `a < b`  |
| `>=`     | Nagyobb vagy egyenlő | `a >= b` |
| `<=`     | Kisebb vagy egyenlő  | `a <= b` |

### 3. Logikai operátorok

| Operátor | Leírás       | Példa                 |
| -------- | ------------ | --------------------- |
| `and`    | Logikai ÉS   | `(a > 0) and (b > 0)` |
| `or`     | Logikai VAGY | `(a > 0) or (b > 0)`  |
| `not`    | Logikai NEM  | `not (a > 0)`         |

## Típusok programozási nyelvekben

Az adott adatoknak (változóknak) fajtái is vannak. Szinte minden programozási nyelvben megtalálhatóak.

### 1. Számtípusok (Numeric Types)

| Típus     | Leírás       | Érték    |
| --------- | ------------ | -------- |
| `int`     | Egész szám   | `-42`    |
| `float`   | Valós szám   | `3.14`   |
| `complex` | Komplex szám | `1 + 2j` |

### 2. Szöveg típus (Text Type)

| Típus | Leírás           | Érték     |
| ----- | ---------------- | --------- |
| `str` | Sztring (szöveg) | `"Hello"` |

### 3. Logikai típus

| Típus  | Leírás                      | Érték  |
| ------ | --------------------------- | ------ |
| `bool` | Logikai érték (igaz, hamis) | `True` |

## Kifejezések

Ezek fontosak lesznek az adott típusokon elvégezhető **műveletek** során.

| Kifejezés        | Érték       |
| ---------------- | ----------- |
| 1+3              | 4           |
| 6\*6-9           | 25          |
| 5 < 6            | True        |
| "téli" + "kabát" | "télikabát" |
| 5 + "let"        | ???         |
| "5" + "let"      | "5let"      |

---

## Változók

Névvel ellátott eltárolt értékek.

- Egyedi, egyszerre egy dolgot képes tárolni!
- Számít a műveletek sorrendje!

### Definíció

```python
ez_egy_valtozo = 1        # értéke 1 (egész szám)
masik_valtozo = "húsleves" # értéke szöveg (string)
hosszu_ez_a_nap = True    # értéke logikai igaz (bool)
```

### Értékadás

```python
kedvenc_szamom = 3                   # létrehozzuk
kedvenc_szamom = kedvenc_szamom + 2  # módosítjuk
```

- Sorrendiség számít!
- Műveletek sorrendje számít!

### Használat – bemenet és kimenet

```python
kedvenc = input("Mi a kedvenc tantárgyad?")
print("A kedvenc tantárgyam: " + kedvenc)
```

### Típusos átalakítás

```python
a = input("a") # 4
b = input("b") # 2
print(a + b)   # "42" – nem összeadás, hanem szöveg összefűzés!
```

```python
a = input("a") # 4
b = input("b") # 2
print("a+b =", int(a) + int(b))  # 6 – most már szám!
```

---

## Szekvencia, Elágazás, Ciklus

### Szekvencia (Sorban végrehajtás)

A program utasításai egymás után, sorban hajtódnak végre, fentről lefelé.

```python
print("Elindult a program")
name = input("Mi a neved? ")
print("Helló, " + name + "!")
print("Program vége")
```

### Elágazás (Döntés – `if`, `else`)

A program bizonyos feltételek alapján más-más utat választ.

```python
a = int(input())

if a % 2 == 0:
    print("páros")
else:
    print("páratlan")
```

### Ciklusok (Ismétlés – `for` és `while`)

#### `for` ciklus – ha tudjuk, hányszor ismételjük:

```python
for i in range(5):  # 0 1 2 3 4
    print("Lépés!", i)
```

#### `while` ciklus – addig fut, amíg a feltétel igaz:

```python
count = 0

while count < 5:
    print("Szám: ", count)
    count += 1
```

A `for` ciklus ismétel egy listán, míg a `while` addig ismétel, amíg egy feltétel igaz.

---

## Feladat

Írjunk egy programot, amely kiszámítja egy kör alapjának területét a megadott sugár alapján.

$$A = \pi \times r^2$$

Ahol \(A\) = terület, \(r\) = sugár, \(\pi \approx 3.14\)

```python
print("Kör alapú henger alap területe")

r = int(input("Add meg a henger alapjának sugarát: 👉 "))
terulet = 3.14 * r * r

print("A kör területe: ", terulet)
```

---

## Feladatok

1. Szorzótábla
2. Celsius–Fahrenheit
3. Szögek, radián
