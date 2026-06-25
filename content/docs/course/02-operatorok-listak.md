---
title: "2. Operátorok, algoritmusok és listák"
weight: 2
draft: false
---

## Ismétlés – Operátorok

Változók létrehozása, módosítása és ellenőrzése

```python
# értékadás
valtozo = 123

# maradékos osztás
valtozo = valtozo % 10
print(valtozo) # 3

# érték változtatás
valtozo = valtozo / 4
print(valtozo) # 0.75

# egyenlőség ellenőrzés
if valtozo == 1:
    print("igaz")
else:
    print("hamis")

# stringek összeadása
kocsi = "rendőr" + "autó"
print(kocsi)

# hogyan ne!
ez = 6
az = "alma"
print(ez + az) # ???
```

---

## Algoritmusok

Algoritmus = recept

- Pontos
- Véges
- Helyes (megengedett utasításokat használja)

### Pszeudokód

![Euklidesz](/img/euklidesz.jpg)

A pszeudokód egy olyan módja annak, hogy leírjuk egy program lépéseit egyszerű, **hétköznapi nyelven**, mintha csak elmesélnénk, mit csináljon a számítógép.

Legnagyobb közös osztó (euklideszi algoritmus):

```
Be: a, b

amíg b nem 0:
    t = b
    b = a % b
    a = t
vége

Ki: a
```

### Folyamatábra

A térkép a programhoz. **Lépésről lépésre!**

Minden alakzat egy külön feladatot vagy döntést jelöl, és a nyilak megmutatják, merre halad tovább a program.

![Folyamatábra](/img/flowchart.png)

---

## Logikai operátorok

### and

Igaz ha *a* **és** *b* is együtt igaz

![and](/svg/and.svg)

### or

Igaz ha *a* **vagy** *b* igaz

![or](/svg/or.svg)

---

## Ciklus vezérlés

### for

Tudjuk, hogy hányszor akarjuk ismételni

```python
for i in range(5):
    print("Lépés:", i)
```

### while

Nem tudjuk előre hányszor akarjuk majd ismételni, de tudjuk mikor fogunk megállni

```python
count = 0
while count < 5:
    print("Lépés:", count)
    count += 1
```

### ![stopsign](/svg/stopsign.svg) break – Vészfék

Amikor meg akarunk állni, mert tudjuk, hogy elértük a célunkat. Működik *for* és *while* esetén is.

```python
correct_password = "python"

while True:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted!")
        break
    print("Wrong password. Try again.")
```

{{< callout type="warning" >}}
A **break** csak egy ciklusból képes kilépni!
{{< /callout >}}

```python
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == 36:
            print("Megvan a 36!")
            break
        print(i, "*", j, "=", i * j)
    print("---")
```

---

## if - else - elif

![fizzbuzz](/svg/fizzbuzz.svg)

*Feladat* – Keressük meg azokat a számokat, amik:

- oszthatóak 3-mal
- oszthatóak 5-tel
- osztható mindkettővel

Mi történik 15-nél?

```python
for i in range(1, 30):
    if i % 3 == 0 and i % 5 == 0:
        print("A(z)" + str(i) + " Osztható mindkettővel")
    elif i % 3 == 0:
        print("A(z)" + str(i) + " Osztható 3-al")
    elif i % 5 == 0:
        print("A(z)" + str(i) + " Osztható 5-vel")
    else:
        print(i)
```

---

## String műveletek

```python
name = input("Hogy hívnak? ")
print("Hello, " + name)
```

### Indexelés és szeletelés

**Fontos:** 0-tól számolunk.

![pythonslices](/svg/pythonslices.svg)

```python
text = "Python"

print(text[0])    # 'P' (első karakter, 0-tól indexelve)
print(text[0:3])  # 'Pyt' (0-tól 2-ig)
print(text[2:])   # 'thon' (2-től a végéig)
print(text[-1])   # 'n' (utolsó karakter)
```

```python
text = "Python"
print(text[:2] + text[2:]) # Python
```

### Bónusz

```python
"ha" * 2 # haha
```

---

## Listák

![shoppinglist](/img/shoppinglist.png)

A lista egy változóban több értéket tárol.

```python
gyumolcsok = ["alma", "banán", "cseresznye"]
```

A listák tartalmazhatnak **szövegeket, számokat** vagy akár más **listákat**.

### Elem elérése index alapján

```python
print(gyumolcsok[0])  # 'alma'
print(gyumolcsok[1])  # 'banán'
print(gyumolcsok[-1]) # 'cseresznye' (utolsó)
```

### Elem módosítása

```python
gyumolcsok[1] = "áfonya"
print(gyumolcsok)  # ['alma', 'áfonya', 'cseresznye']
```

### Elem hozzáadása

```python
gyumolcsok.append("narancs")    # Hozzáadás a végéhez
gyumolcsok.insert(1, "kiwi")    # Beszúrás az 1-es helyre
```

### Elem eltávolítása

```python
gyumolcsok.remove("alma")  # Törlés érték alapján
gyumolcsok.pop(0)          # Törlés index alapján
```

### Lista bejárása ciklussal

![search](/img/search.jpg)

```python
for gyumolcs in gyumolcsok:
    print("Szeretem a", gyumolcs)
```

Lista hossza:

```python
len(gyumolcsok) # 3
```

A `range()` is listát ad vissza:

```python
for i in range(5): # 0,1,2,3,4
    print(i)
```

---

## Listák másolása

![copy](/img/copy.jpg)

Ha egy listát másolsz egyenlőséggel (`=`), nem új listát kapsz – mindkét változó ugyanarra a listára mutat.

```python
eredeti = [1, 2, 3]
masolat = eredeti

masolat[0] = 99
print(eredeti)  # [99, 2, 3] ❌
```

### Helyes másolás

`list()` függvénnyel:

```python
eredeti = [4, 5, 6]
masolat = list(eredeti)
```

`copy()` metódussal:

```python
eredeti = [7, 8, 9]
masolat = eredeti.copy()
```

{{< callout type="warning" >}}
Ez a másolat csak a felső szintet másolja. Ha listád listákat tartalmaz, azokat nem másolja!
{{< /callout >}}

### Beépített lista műveletek

```python
szamok = [3, 5, 7]
eredmeny = sum(szamok)
print(eredmeny)  # 15
```

| Függvény        | Leírás                         |
| --------------- | ------------------------------ |
| `sum(lista)`    | Összeadja az elemeket          |
| `len(lista)`    | Megadja az elemek számát       |
| `min(lista)`    | Legkisebb értéket adja vissza  |
| `max(lista)`    | Legnagyobb értéket adja vissza |
| `sorted(lista)` | Új, rendezett listát ad vissza |

### Lista határain kívül

```python
gyumolcsok = ["alma", "banán", "cseresznye"]
print(gyumolcsok[3])  # ❌ Hiba!
```

```
IndexError: list index out of range
```

---

## A stringek úgy viselkednek, mint a listák

*Feladat* – írjunk szöveget függőlegesen:

```python
szoveg = input()

i = 0
while i < len(szoveg):
    print(szoveg[i])
    i += 1
```

**DE** a string elemeit nem lehet módosítani:

```python
szoveg[0] = "J"  # ❌ Hibát dob
```

Új stringet kell létrehozni:

```python
szoveg = "J" + szoveg[1:]
print(szoveg)  # 'Jython'
```

---

## Feladatok

### 1. Minimum és maximum

Keressük meg egy listában a legkisebb és a legnagyobb értéket.

<details>
<summary>Megoldás</summary>

```python
numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("Maximum:", max_num)
```

</details>

### 2. Átlag és medián

Számoljuk ki egy lista elemeinek átlagát és mediánját.

**Átlag (számtani közép):**

$$\text{átlag} = \frac{\sum_{i=1}^{n} x_i}{n}$$

**Medián:**

Páratlan elemszám esetén: \(\text{medán} = x_{\frac{n+1}{2}}\)

Páros elemszám esetén: \(\text{medán} = \frac{x_{\frac{n}{2}} + x_{\frac{n}{2} + 1}}{2}\)

<details>
<summary>Megoldás</summary>

```python
numbers = [5, 3, 8, 6, 2]
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Összeg:", total)
print("Átlag:", average)

numbers.sort()
n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("Medián:", median)
```

</details>

### 3. Lineáris keresés

Keressünk meg egy adott számot egy listában.

<details>
<summary>Megoldás</summary>

```python
numbers = [4, 8, 1, 6]
target = 6
found = False

for n in numbers:
    if n == target:
        found = True
        break

if found:
    print("Megvan!")
else:
    print("Nincs benne a listában.")
```

</details>

### 4. Fordítsunk meg egy listát

<details>
<summary>Megoldás</summary>

```python
text = "hello"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)
```

</details>

### 5. (Extra) Rendezés 🤔

Írjunk egy programot, ami képes egy listát növekvő sorrendbe rendezni.

<details>
<summary>Megoldás</summary>

```python
# Buborék rendezés
szamok = [5, 3, 8, 1, 4]
n = len(szamok)

for i in range(n):
    for j in range(n - 1):
        if szamok[j] > szamok[j + 1]:
            szamok[j], szamok[j + 1] = szamok[j + 1], szamok[j]

print("Rendezett lista:", szamok)
```

</details>
