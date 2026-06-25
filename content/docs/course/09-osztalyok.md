---
title: "9. Osztályok és objektumorientált programozás"
weight: 9
draft: false
---

## Osztályok és függvények Pythonban

A Pythonban az osztályok és a függvények alapvető fogalmak, amelyek segítenek a kód rendszerezésében és felépítésében. A cél az **újrafelhasználhatóság** és **moduláris kód** létrehozása.

Az osztályok lehetővé teszik, hogy sablonokat használjunk, amelyek adatokat és/vagy viselkedést tárolnak.

Ez egy módot ad arra, hogy a kapcsolódó adatokat (**attribútumokat**) és függvényeket (**metódusokat**) egyetlen egységbe foglaljuk. Osztályok használatával **példányokat (objektumokat)** hozhatunk létre, amelyek mindegyike saját, egyedi adathalmazzal rendelkezik.

### Hogyan kapcsolódnak ide a függvények?

A függvények ezzel szemben újrahasznosítható kódrészletek, amelyek meghatározott feladatokat végeznek el. Segítenek a bonyolult problémák kisebb, kezelhetőbb részekre bontásában.

---

## Készítsünk osztályt

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method1(self):
        pass  # Method implementation

    def method2(self):
        pass  # Method implementation
```

```python
myinstance = ClassName("val1", "val2")
myinstance.method1()
myinstance.method2()
```

## Valós példa

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
```

```python
dog1 = Dog("Bodri", 3)
dog1.bark()  # Bodri says woof!
```

### Kulcsfogalmak:

- A `class` az osztályt definiálja.
- Az `__init__()` a konstruktor, automatikusan lefut, amikor egy objektumot létrehozunk.
- A `self` az aktuális példányra utal.

Minden objektumnak saját adatai vannak.

---

## Öröklés (Inheritance)

Az öröklés segítségével egy osztály átveheti egy másik osztály tulajdonságait és metódusait.

```python
class Animal:
    def speak(self):
        return ""

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"
```

## Polimorfizmus (Polymorphism)

Ugyanaz a metódusnév különböző osztályokban különbözőképpen viselkedhet.

```python
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())
```

## Kompozíció (Composition)

Egy osztály más osztályok példányait tartalmazza.

```python
class Engine:
    def __init__(self, type):
        self.type = type

class Car:
    def __init__(self):
        self.engine = Engine("v8")  # composition
```

---

## Összefoglalás

| Fogalom         | Leírás                                                        |
| --------------- | ------------------------------------------------------------- |
| **Osztály**     | Sablon objektumok létrehozásához                              |
| **Objektum**    | Az osztály egy példánya, saját adatokkal                     |
| **Attribútum**  | Az objektum adatai (`self.name`)                             |
| **Metódus**     | Az objektum viselkedése (`def bark(self)`)                   |
| **Öröklés**     | Egy osztály átveszi egy másik tulajdonságait                 |
| **Polimorfizmus**| Ugyanaz a metódusnév, különböző viselkedés különböző osztályban |
| **Kompozíció**  | Osztály más osztályok példányait tartalmazza                 |
