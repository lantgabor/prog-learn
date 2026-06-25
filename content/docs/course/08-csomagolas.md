---
title: "8. Modulok és alkalmazás-csomagolás"
weight: 8
draft: false
---

## Több fájlos programok

```python
# jatek.py - Itt van a fő játék
from kerdesek import kerdes_lista

def indit_jatek():
    print("Kezdődik a játék!")
    for kerdes in kerdes_lista:
        print(kerdes)

indit_jatek()
```

```python
# kerdesek.py - Itt tároljuk a kérdéseket
kerdes_lista = [
    "Mi a kedvenc színed?",
    "Szereted a pizzát?",
    "Hány éves vagy?"
]
```

### Hogyan működik?

1. Minden fájl egy kis doboz
2. Az `import` paranccsal kinyitjuk a dobozt
3. Használhatjuk, ami benne van!

---

## Fordítás (Compiling)

Hogyan lesz a kód a számítógép számára érthető.

![compiler](/img/compiler.png)

1. **Compiled languages:** Szó szerint érthető fordítás, latinról → angolra.
2. **Interpreted languages:** Melleted ül valaki aki helyben fordít.

### Mi történik a kóddal?

Képzeld el, hogy megírtál egy szuper programot, de hogyan lesz ebből olyan alkalmazás, amit a barátaid is tudnak használni a saját számítógépükön?

{{< steps >}}

### Forráskód
Ez amit te írsz (pl. `.py` fájlok)

### Fordítás/Értelmezés
A számítógép számára érthető formába alakítás

### Csomagolás
Minden szükséges dolog összegyűjtése egy csomagba

### Terjesztés
A program eljuttatása más felhasználókhoz

{{< /steps >}}

### Mit csomagolunk valójában?

Egy játék esetén nem csak a játék kódját tartalmazza – kellenek még:

- Képek, hangok, szövegek
- Extra programok (függőségek)
- Beállítások

---

## Hogyan lesz a programból alkalmazás?

Képzeljük el, hogy sütit sütünk! 🍪

### Mi kell hozzá?

1. **A recept (forráskód)**
   - A Python fájljaink (`.py`)
   - Képek, hangok, szövegek

2. **Hozzávalók (eszközök)**
   - PyInstaller – Ez csinál a programból alkalmazást
   - Extra programok, amiket használunk

### Hogyan csináljuk?

```bash
# 1. Telepítjük a PyInstaller-t
pip install pyinstaller

# 2. Elkészítjük az alkalmazást
pyinstaller --onefile jatek.py
```

És kész is! 🎉 A `dist` mappában megtalálod az alkalmazást.

---

## Mit kapunk végül?

Attól függ, milyen gépen használod:

| Operációs rendszer | Eredmény            |
| ------------------ | ------------------- |
| Windows            | Egy `.exe` fájl     |
| Mac                | Egy `.app` program  |
| Linux              | Egy futtatható fájl |

## Próbáljuk ki!

Csináljunk egy egyszerű programot és csomagoljuk be:

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
```

{{< callout type="warning" >}}
Az `input()` a program végén azért szükséges, mivel a program végeztével azonnal kilépünk a **console**-ból!
{{< /callout >}}

```bash
pyinstaller --onefile kviz.py
```

Kész is!
