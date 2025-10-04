from mymodule1 import lista
from mymodule2 import mymodule2


def main():
    print("Hello, World!")
    print("List from mymodule1:", lista)
    print("List from mymodule2:", mymodule2.my_function())
    print("Constant LISTA3 from mymodule2:", mymodule2.lista3)


if __name__ == "__main__":
    main()  # your program logic
    input("\nPress Enter to exit...")
