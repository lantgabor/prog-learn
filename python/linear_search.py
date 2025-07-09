numbers = [4, 8, 1, 6]
print(numbers)
target = 6
print("Keresett szám:", target)
found = False

for n in numbers:
    if n == target:
        found = True
        break

if found:
    print("Found!")
else:
    print("Not found.")
