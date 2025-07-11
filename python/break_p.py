for i in range(1, 10):
    for j in range(1, 10):
        if i * j == 36:
            print("Megvan a 36!")
            break
        print(i, "*", j, "=", i * j)
    print("---")
