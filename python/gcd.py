# Euclidean algorithm
a = int(input("a? "))
b = int(input("b? "))

while b != 0:
    t = b
    b = a % b
    a = t

print("gcd =", a)