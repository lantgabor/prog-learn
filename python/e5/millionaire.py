questions = [
    ("What is the capital of France?", ["Paris", "Rome", "Madrid", "Berlin"], "A"),
    (
        "Who created the Python programming language?",
        ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"],
        "A",
    ),
    ("What is 5 in binary?", ["110", "1001", "101", "111"], "C"),
    (
        "What does HTTP stand for?",
        [
            "Hyperlink Text Transmission",
            "Hypertext Transfer Protocol",
            "High Transfer Text Protocol",
            "Hypertext Transport Protocol",
        ],
        "B",
    ),
    (
        "Which is the largest planet in our Solar System?",
        ["Earth", "Saturn", "Mars", "Jupiter"],
        "D",
    ),
    (
        "Was the year 2000 a leap year?",
        ["Yes", "No", "Only in the EU", "Only in the US"],
        "A",
    ),
    (
        "What is the standard file extension for Python modules?",
        [".py", ".python", ".p", ".pt"],
        "A",
    ),
    (
        "Time complexity of binary search on a sorted array?",
        ["O(n)", "O(n log n)", "O(log n)", "O(1)"],
        "C",
    ),
    (
        "Which Git command copies a remote repository locally?",
        ["git clone <url>", "git pull", "git init", "git fork"],
        "A",
    ),
    ("What is 2**10?", ["1000", "1024", "512", "2048"], "B"),
]


prizes = [1_000, 5_000, 10_000, 25_000, 50_000, 100_000, 250_000, 500_000, 750_000, 1_000_000]

for i in prizes:
    print(i)

nyeremeny = 0
vesztes = False



while not vesztes and nyeremeny < 1_000_000:
    for i, (kerdes, valaszok, helyes) in enumerate(questions):
        print(f"\nForint: {prizes[i]}")
        print(f"Kérdés: {kerdes}")
        print(f"A: {valaszok[0]}")
        print(f"B: {valaszok[1]}")
        print(f"C: {valaszok[2]}")
        print(f"D: {valaszok[3]}")

        valasz = input("Válasz (A/B/C/D): ").upper()

        if valasz == helyes:
            nyeremeny = prizes[i]
            print(f"Helyes! Nyereményed eddig: {nyeremeny} Forint")
            if nyeremeny == 1_000_000:
                print("Gratulálok! Te vagy a főnyertes!")
                break
        else:
            vesztes = True
            print(f"Helytelen válasz. Végső nyereményed: {nyeremeny} Forint")
            break
