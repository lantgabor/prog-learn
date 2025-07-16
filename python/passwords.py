correct_password = "python"

while True:
    guess = input("Enter password: ")
    if guess == correct_password:
        print("Access granted!")
        break
    if guess == "exit":
        print("Exiting...")
            
    print("Wrong password. Try again.")