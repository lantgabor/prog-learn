# gyakorolhatjuk a for vs while lehetőségeit
# + 
# gyakorolhatjuk az else if elif tulajdonságait

for i in range(1, 30):
    if i % 3 == 0 and i % 5 == 0:
        print("A(z)" + str(i) + " Osztható mindkettővel")
    elif i % 3 == 0:
        print("A(z)" + str(i) + " Osztható 3-al")
    elif i % 5 == 0:
        print("A(z)" + str(i) + " Osztható 2-vel")
    else:
        print(i)

