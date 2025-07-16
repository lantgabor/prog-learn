# Euclidean algorithm
a = int(input("a? "))
b = int(input("b? "))

while b != 0:
    print("---")
    t = b
    print("t =", t)
    b = a % b
    print("b =", b)
    a = t
    print("a =", a)

print("gcd =", a)