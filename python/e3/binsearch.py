names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = "Diana"

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

print(found)  # Will print index or -1 if not found
