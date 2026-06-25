---
title: "6. Gyakorlás – A Milliomos játék"
weight: 6
draft: false
---

## Ismétlés

- **Függvények**
  - Új képességet adunk a Python-nak → névvel újrahasználható
  - Példák: `koszont()`, `negyzet(x)`
  - Felépítés: `def` + név + paraméterek + utasítások
  - `return` kulcsszó → visszatérés eredménnyel

- **Lokális változók**
  - Csak a függvényben élnek, futás után megszűnnek
  - Globális vs. Lokális változók

- **Procedurális/hierarchikus programozás**
  - Függvények → színészek 🎭
  - `main()` → főszereplő
  - `seged()` → mellékszereplő
  - `if __name__ == "__main__":` → csak közvetlen futtatásnál indul el a `main()`

---

## Egészítsük ki a múltkori programot

A "Legyen Ön is Milliomos" játékon dolgozunk tovább. A program struktúrája:

{{< steps >}}

### `main()` függvény
A teljes játékmenet irányítása.

### `betoltes()` függvény
- Kérdések betöltése
- Játékállás betöltése
- Ranglista betöltése

### `mentes()` függvény
- Ranglista mentése

### Segítő függvények
- Felezés
- Közönség segítség
- Feladás (nyereményhatárok, jelenlegi elért összeg)

{{< /steps >}}

A program jó struktúrája:

```python
def main():
    kerdesek = betoltes()
    pontszam = 0
    jatssz(kerdesek, pontszam)

def betoltes():
    return [
        {"kerdes": "Mi a Python?", "valasz": "Programozási nyelv"},
        # ...
    ]

def jatssz(kerdesek, pontszam):
    for kerdes in kerdesek:
        print(kerdes["kerdes"])
        valasz = input("Válasz: ")
        if valasz == kerdes["valasz"]:
            pontszam += 1
            print("✅ Helyes!")
        else:
            print("❌ Helytelen!")
    print(f"Végső pontszám: {pontszam}")

if __name__ == "__main__":
    main()
```
