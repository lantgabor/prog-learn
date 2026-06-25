---
title: "Extra feladatok"
weight: 11
draft: false
---

## Feladatok

### Étlap formázása

Írj egy programot, amely szépen formázva kiír egy heti menzai étlapot!
Használj benne speciális karaktereket:

- `\t` → tabulátor (behúzás)
- `\n` → új sor
- `\\` → visszaperjel megjelenítése

### Téglalap rajzolása karakterekkel

```python
szelesseg = int(input("Add meg a téglalap szélességét: "))
magassag = int(input("Add meg a téglalap magasságát: "))

# Felső szegély
print("+" + "-" * szelesseg + "+")

# Középső sorok
for _ in range(magassag - 2):
    print("|" + " " * szelesseg + "|")

# Alsó szegély, ha magasság legalább 2
if magassag >= 2:
    print("+" + "-" * szelesseg + "+")
```

---

## Programozási feladatok

1. Pénzváltó program
2. Legkisebb közös többszörös
3. Faktoriális
4. Python Turtle – kör, háromszög, pizza
5. Python debugger (`pdb`) lépésről lépésre

---

## Algoritmikus feladatok

### Múzeum I.

Egy múzeumban kíváncsiak arra, a hét mely napján van a legtöbb látogató. Ehhez több hét adatait feldolgozzák.

Írj programot, amely a szabványos bemenetén fogadja a múzeum napi látogatási adatait úgy, hogy soronként a hét napjának sorszámát kapjuk 0-6 között, majd szóközzel elválasztva a látogatók számát. Az adatok rendezetlenül érkeznek, adott sorszámú naphoz több bejegyzés is tartozhat. A bemenet végét üres sor jelzi.

Írja ki a program a szabványos kimenetre annak a napnak a sorszámát, amely a legtöbb látogatót jelenti. Feltételezzük, hogy egy ilyen nap van.

---

### Múzeum II.

Egy múzeumban gazdasági okok miatt heti egy szünnapot szeretnének tartani, ezért keresik a hét azon napját, amikor a legkevesebb a látogató.

Írj programot, amely a szabványos bemenetén fogadja a múzeum napi látogatási adatait úgy, hogy soronként a hét napjának sorszámát kapjuk 1-7 között, majd szóközzel elválasztva a látogatók számát. Az adatok rendezetlenül érkeznek, adott sorszámú naphoz több bejegyzés is tartozhat. A bemenet végét üres sor jelzi.

Írja ki a program a szabványos kimenetre annak a napnak a sorszámát, amely a legkevesebb látogatót jelenti. Feltételezzük, hogy egy ilyen nap van.

---

## Egyéb feladatok

- A `while`-ra egy példa: lottószám sorsolás (ugyanaz a szám nem szerepelhet kétszer, `while i <= 5`)
- Algoritmus: telefonkönyv keresés – egyesével, kettesével, bináris keresés
