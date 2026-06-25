---
title: "5. Függvények"
weight: 5
draft: false
---

## Ismétlés

- **Debugger**
  - Lépésenkénti futtatás
  - Változók figyelése
  - Hibák forrásának felderítése
  - Breakpoint, végrehajtás irányítása

- **Pszeudovéletlen számok**
  - Álvéletlenszám-generátor
  - `random.randint()`
  - Láva lámpa példa

---

## Függvények

Képzeld el, hogy van egy robotod.

Meg tudod tanítani, hogy végezzen el egy feladatot egyszer, adj neki egy nevet, és onnantól kezdve, amikor csak szükséged van rá, elég csak a nevét "hívni" – nem kell mindig újra leírnod.

Pontosan ezt csinálják a függvények a Pythonban:
➡️ Új "képességet" tanítasz a Python-nak, és nevet adsz neki, így bármikor újra használhatod.

```python
def koszont():
    print("Helló, világ!")

koszont()
```

Valami hasznosabb:

```python
def negyzet(x):
    return x * x

print(negyzet(5))  # 25
```

## Függvények felépítése

```python
def fuggveny_nev(parameterek):
```

- `def` → **kulcsszó**, ami azt jelenti: „Most definiálok egy függvényt."
- `fuggveny_nev` → **a függvény neve** (mint amikor elnevezed a robotodat).
- `(parameterek)` → kis dobozok az információnak, **amit a függvény kaphat**.
- `:` → jelzi a Python-nak: „Most jönnek az utasítások."

## Return

A függvények néha nem csak csinálnak valamit (pl. kiírnak szöveget), hanem vissza is adnak egy eredményt.
Ehhez használjuk a `return` kulcsszót.

```python
def osszead(a, b):
    return a + b

eredmeny = osszead(3, 5)
print(eredmeny)  # 8
```

---

## Lokális változók

A robotodnak van egy kis saját fiókja.
Amikor a robot dolgozik, ebbe a fiókba teszi azokat a változókat, amiket csak ő ismer.
Ezeket nevezzük **lokális változóknak**.

{{< callout type="info" >}}
A lokális változó csak abban a függvényben él, ahol létrehoztad.  
Amint a függvény lefut, a változó eltűnik – mintha a robot lezárná a fiókját.
{{< /callout >}}

```python
def szorzas():
    eredmeny = 3 * 5   # lokális változó
    print("Az eredmény:", eredmeny)

szorzas()
print(eredmeny)  # ❌ hiba!
```

### Globális vs. Lokális

- **Globális változó** → mindenki látja (a teljes programban).
- **Lokális változó** → csak a függvény látja, ahol létrejött.

---

## Procedurális/hierarchikus programozás

Képzeld el, hogy a programod egy színdarab 🎭.

- A függvények = a színészek, akik tudnak különböző dolgokat.
- A `main` függvény = a főszereplő, aki elindítja a darabot, és megmondja, milyen sorrendben történjenek a dolgok.

```python
def main():
    print("Helló, én vagyok a főszereplő!")
    seged()

def seged():
    print("Én pedig egy mellékszereplő vagyok.")

if __name__ == "__main__":
    main()
```

### Mit jelent az `if __name__ == "__main__":`?

Ez egy varázsformula ✨, ami azt mondja:

> „Ha közvetlenül futtatod ezt a fájlt, indítsd el a `main()`-t!"

Ha viszont csak importálod a fájlt máshonnan, akkor nem fut el automatikusan a `main()`.

---

## Feladatok

1. Legyen Ön is Milliomos
2. Hatos lottó
3. Telefonkönyv keresés
