---
title: "4. Debugger és véletlenszámok"
weight: 4
draft: false
---

## Ismétlés

1. **Tízes számrendszer** működése és számítási logikája.
2. **Bináris számrendszer:** alapok, bit és bájt fogalma, összeadás, kivonás, szorzás, osztás binárisan.
3. **Pythonban** bináris–decimális átváltás: `0b111011`, `bin()`
4. **ASCII kód:** betűk és szimbólumok számbeli (bináris) ábrázolása – `ord()` és `chr()` függvények.
5. ASCII művészet és a hacker kultúrában való használat.
6. Bitméretek jelentősége: 8, 16, 32 bit kapacitás.
7. **Unicode:** globális karakterkészlet – nyelvek, ékezetek, szimbólumok, emojik.
8. **Emojik:** Unicode-kódolás, használat programban.
9. RGB színrendszer: 24 bites színábrázolás, 16,7 millió szín.
10. **Videó:** képkockák sorozata, 24–60 FPS.
11. **Hang:** mintavételezés, például 44,1 kHz.

---

## Debugger

**Lépésenkénti futtatás** – Nem kell a teljes programot újraindítani, megnézheted, pontosan hol mi történik.

**Változók figyelése** – Láthatod a program aktuális állapotát, változókat és objektumokat.

**Hibák forrásának felderítése** – Könnyen megtalálhatod, hol tér el a program a várt működéstől.

### Hogyan működik?

| Funkció                 | Leírás                                                     |
| ----------------------- | ---------------------------------------------------------- |
| **Breakpoint**          | A program ezen a soron megáll.                             |
| **Step over**           | Következő sorra lép, de nem megy bele a függvényhívásokba. |
| **Step into**           | Belép a függvénybe és ott folytatja a lépést.              |
| **Step out**            | Kilép az aktuális függvényből a hívóhoz.                   |
| **Continue**            | Folytatja a futást a következő breakpointig.               |
| **Watch**               | Kijelölt változó értékének figyelése.                      |
| **Evaluate expression** | Tetszőleges kifejezés kiértékelése futás közben.           |

### Tipikus hibakeresési folyamat

{{< steps >}}

### Töréspontok beállítása
Oda, ahol gyanítod a hibát.

### Program indítása debugger módban

### Kód végiglépkedése
Figyelve a változókat és a vezérlés útját.

### Elemzés
Hol tér el a tényleges érték a várttól?

### Hiba javítása
Kód módosítása.

### Újra futtatás
Ellenőrzés, hogy megszűnt-e a probléma.

{{< /steps >}}

Hasznos online eszközök:
- [pythontutor.com](https://pythontutor.com/render.html#mode=display) – kód vizualizáció
- [pyodide.org](https://pyodide.org/en/stable/console.html) – Python a böngészőben

---

## Pszeudovéletlen számok

![numbers](/img/numbers-crunching.gif)

A számítógép nem tud igazán véletlenszerű lenni.

Ezért álvéletlenszám-generátorokat használ, amelyek úgy tűnnek, mintha véletlenszerűek lennének.

```python
import random
print(random.randint(1, 10))
```

[Hogyan működnek a véletlenszám-generátorok?](https://www.youtube.com/watch?v=1cUUfMeOijg)

![lavalamp](/img/lavalamp.jpg)

## Python Lottószámok

```python
import random
lottery = random.sample(range(1, 50), 6)
print("🎟️ Your numbers:", lottery)
```

Hagyd, hogy a Python válassza ki a szerencseszámaidat 🎲

---

## Keresés nevek között: Lineáris vs Bináris

![phonebook](/img/phonebook.jpg)

```python
names = ["Adam", "Béla", "Cecil", "Dóri", "Erik"]
```

### Lineáris keresés

Minden elemet megnézünk sorban:

```python
for name in names:
    if name == "Dóri":
        print("Found!")
```

### Bináris keresés

Felezzük a keresési teret minden lépésben (csak rendezett listán működik!):

```python
target = "Dóri"

low = 0
high = len(names) - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if names[mid] == target:
        found = mid
        break
    elif names[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(found)  # Index, vagy -1 ha nem találtuk
```

{{< callout type="info" >}}
Lineáris keresés = egyesével ellenőriz 🐢 (lassú)  
Bináris keresés = felez és hódít ⚡ (gyorsabb – de rendezett adatok kellenek!)
{{< /callout >}}

---

## Feladatok

1. Számoljuk meg a szövegben található kisbetűk számát.
2. Caesar-féle kódolás – [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
3. Kő – papír – olló?
4. Hányszor szerepelnek a magánhangzók a szövegben?
5. Utolsó N szám átlaga
6. Leibniz formula – [Wikipedia](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
