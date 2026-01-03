class ceruza:
    def __init__(self, szin) -> None:
        self.szin = szin

    def kiir(self):
        print(self.szin)


ceruza1 = ceruza("piros")
ceruza2 = ceruza("sarga")

print(ceruza1.szin)
print(ceruza2.szin)

ceruza1.kiir()
ceruza2.kiir()
