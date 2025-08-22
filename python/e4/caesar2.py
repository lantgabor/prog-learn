# A kódoló:

kulcs = input("Melyik karakterrel kódoljunk? (a-z) ")
while len(kulcs) != 1 or ord(kulcs) < ord("a") or ord(kulcs) > ord("z"):
    kulcs = input("Melyik karakterrel kódoljunk? (a-z) ")

delta = ord(kulcs) - ord("a")
print(delta)

szoveg = input("Írd be a kódolandó szöveget: ")
kodolt = ""

for i in szoveg:
    if ord(i) < ord("a") or ord(i) > ord("z"):
        kodolt += i
        continue

    eltolas = ord(i) + delta
    while eltolas > ord("z"):
        eltolas = eltolas - (ord("z") - ord("a") + 1)

    kodolt += chr(eltolas)

print(kodolt)
# A dekódoló ugyanez, csak kivonni kell, és a másik irányba történhet „túlcsordulás”:

kulcs = input("Melyik karakterrel dekódoljunk? (a-z) ")
while len(kulcs) != 1 or ord(kulcs) < ord("a") or ord(kulcs) > ord("z"):
    kulcs = input("Melyik karakterrel kódoljunk? (a-z) ")

delta = ord(kulcs) - ord("a")
print(delta)

szoveg = input("Írd be a kódolandó szöveget: ")
kodolt = ""

for i in szoveg:
    if ord(i) < ord("a") or ord(i) > ord("z"):
        kodolt += i
        continue

    eltolas = ord(i) - delta
    while eltolas < ord("a"):
        eltolas = eltolas + (ord("z") - ord("a") + 1)

    kodolt += chr(eltolas)

print(kodolt)
