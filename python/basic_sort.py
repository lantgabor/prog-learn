numbers = [5, 2, 8, 1]
print(numbers)
n = len(numbers)

for i in range(n):
    for j in range(n - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)
