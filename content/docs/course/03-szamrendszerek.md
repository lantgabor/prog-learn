---
title: "3. Számrendszerek és kódolás"
weight: 3
draft: false
---

## A tízes számrendszer: Amit megszoktunk

![counting](/img/count.gif)

Tíz ujjunk van, így a számolási rendszerünk—amit tízes számrendszernek hívunk—a 10 hatványain alapul:

```
Places:   10^2   10^1   10^0
Value:     100     10      1
Example:     3      2      5 → 3*100 + 2*10 + 5 = 325
```

Így gondolkodunk mi — de nem így gondolkodnak a számítógépek.

![Decimal digit](/img/Decimal_digit.png)

---

## Bináris: A gépek nyelve

![binary](/svg/binary.svg)

A számítógépek a bináris számrendszert használják, amely egy kettes alapú rendszer, mindössze két számjeggyel: **0** és **1**.

```
Places:   2^3  2^2  2^1  2^0
Value:      8    4    2    1
Binary:     1    0    1    1 → 1*8 + 0*4 + 1*2 + 1*1 = 11
```

Minden egyes **1**-es vagy **0** egy bit.
Gondolj a bitre úgy, mint egy kapcsolóra: **BE** vagy **KI.**

8 bit = 1 bájt.

![Binary counter](/img/Binary_counter.gif)

### Összeadás

Tízes számrendszerhez hasonlóan:

```
   1011   (11 in decimal)
+  1101   (13 in decimal)
-------
 11000   (24 in decimal)
```

```python
a = 0b1011
b = 0b1101
print(bin(a + b))  # 0b11000
```

### Kivonás

```
   1010   (10)
-  0011   ( 3)
-------
   0111   ( 7)
```

```python
a = 0b1010
b = 0b0011
print(bin(a - b))  # 0b111
```

### Szorzás

```
    101   (5)
  x  11   (3)
  ------
    101   (5 * 1)
+ 1010    (5 * 1 shifted)
-------
  1111   (15)
```

```python
a = 0b101
b = 0b11
print(bin(a * b))  # 0b1111
```

### Osztás

```
1100 ÷ 10  → 6
= 0b1100 ÷ 0b10 = 0b110
```

```python
a = 0b1100
b = 0b10
print(bin(a // b))  # 0b110
print(bin(a % b))   # 0b0 (remainder)
```

---

## Kódolási kihívás: Bináris ↔ Decimális

Bináris és decimális számok közötti átváltás Pythonban:

```python
# Decimal to binary
print(bin(42))  # 0b101010

# Binary to decimal
print(int("101010", 2))  # 42
```

Próbáld meg átváltani a korodat, a szerencseszámodat, vagy akár a telefonszámod egy részét binárisra!

Készítsünk bináris órát!

---

## ASCII: Amikor a betűk találkoznak a binárissal

```
O     O           ,       
  o o          .:/    
    o      ,,///;,   ,;/ 
      o   o)::::::;;///
         >::::::::;;\\\ 
           ''\\\\\'" ';\ 
              ';\
```

Az ASCII az „American Standard Code for Information Interchange" rövidítése.

Minden betűhöz vagy szimbólumhoz tartozik egy szám:

```
A → 65
a → 97
! → 33
```

Ezek a számok binárisan vannak tárolva!

Kedvenc állatod: [asciiart.eu](https://www.asciiart.eu/animals)

![ASCII table](/img/asciitable.png)

---

## Python + ASCII: `ord()` és `chr()`

```python
print(ord('A'))  # 65
print(chr(66))   # B
```

Próbáld ki: írasd ki a neved betűnként, és kérd le az ASCII értékeiket!

`1100110 1110010 1101001 1100100 1100001 1111001`

## ASCII Művészet: Rajzolás karakterekkel

Az ASCII art az ősi mesterség, amikor csak szövegkarakterek segítségével készítünk képeket.

`:-)     (•_•)     (╯°□°）╯︵ ┻━┻`

Régi videojátékokban, terminálokban és a „hacker kultúrában" is használták – és ma is menő!

---

## Bitek és tárolás

![thinking](/img/thonks.png)

- 8 bit = 256 érték (0–255)
- 16 bit = 65 536 érték
- 32 bit = több mint 4 milliárd különböző érték!

Minél több bitünk van, annál több dolog fér el: több betű, több hang, több szín, és igen — több emoji is! 🎨🎧

---

## Unicode: ASCII Nagy Testvére

![unicode](/img/unicode.jpg)

A Unicode kibővíti az ASCII-t, hogy minden nyelvet, írásrendszert és emojit is tartalmazzon.
Támogatja például:

- Ékezeteket: é, ñ, ü
- Nyelveket: arab, hindi, kínai
- Emojikat és szimbólumokat is!

```python
print("こんにちは")  # Japanese
```

## Emojik = Unicode varázslat ✨

Igen, az emojiknak is van Unicode-kódjuk!

```python
print("\U0001F602")  # 😂
```

Ezért tudod őket használni üzenetekben, weboldalakon vagy akár a saját programodban is.

Minden évben új emojik jelennek meg: [emojipedia.org/new](https://emojipedia.org/new)

---

## Színek bitekben

![gato-rgb](/img/gato-rgb.gif)

A képernyőn megjelenő színek az RGB rendszert használják:

- **R**ed – piros
- **G**reen – zöld
- **B**lue – kék

Mindhárom csatorna 8 bitet használ: értékek 0-tól 255-ig.

```python
r, g, b = 255, 0, 0  # Pure red
```

🖌️ 24 bit = 16,7 millió színkombináció!

![tvstore](/img/tvstore.jpg)

---

## Videók = Képek + Idő

A videók nem mások, mint gyors egymásutánban megjelenített képek (ún. képkockák).

Ha másodpercenként 24–60 képet látunk, az agyunk mozgást érzékel!

![flipbook animation](/img/flipbook-animation.gif)

---

## Hang és zene a számítógépben

A hang hullámformákból áll, amit a gép mintavételez – nagyon gyorsan számokká alakítva.

Például: 44 100 minta másodpercenként egy tipikus zenei hangfájl esetén!

![Frequency vs name](/svg/Frequency_vs_name.svg)

---

## Emojik programozása Pythonban

```python
emojis = ["😀", "🐍", "🚀", "🍕"]
for emoji in emojis:
    print(emoji * 5)
```

Készíthetsz emoji zászlót, szegélyt vagy akár 100-szor is kiprintelheted a kedvencedet 😎
