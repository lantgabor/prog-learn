import random, os

SCORES_FILE = "/Users/gaborlant/work/prog-learn/python/e7/scores.txt"

def ask(q, opts, correct, lifeline):
    print(q)
    for i, o in enumerate(opts, 1):
        print(f"{i}. {o}")
    if lifeline:
        print("Type '50' to use 50:50 lifeline")
    ans = input("Your answer (1-4 or 50): ")

    if ans == "50" and lifeline:
        wrong_options = [i for i in range(1, 5) if i != correct]
        extra_keep = random.choice(wrong_options)
        keep = [correct, extra_keep]

        print("\n50:50 used! Remaining:")
        for i, o in enumerate(opts, 1):
            if i in keep:
                print(f"{i}. {o}")
        ans = input("Your answer (1-4): ")
        return ans == str(correct), False

    return ans == str(correct), lifeline

def prize(n):
    prizes = [
        100, 200, 300, 500, 1000, 2000, 4000,
        8000, 16000, 32000, 64000, 125000,
        250000, 500000, 1000000
    ]
    return prizes[n]

def load_scores():
    scores = []
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE) as f:
            for line in f:
                line = line.strip()
                if line:  # ignore empty lines
                    parts = line.split(",")
                    name = parts[0]
                    score = int(parts[1])
                    scores.append((name, score))
    return scores

def save_score(name, score):
    with open(SCORES_FILE, "a") as f:
        f.write(f"{name},{score}\n")

def show_top(scores):
    # Sort scores manually (highest first)
    sorted_scores = sorted(scores, key=lambda item: item[1], reverse=True)

    print("\n🏆 Top 10 Scores 🏆")
    rank = 1
    for entry in sorted_scores[:10]:
        player_name = entry[0]
        player_score = entry[1]
        print(f"{rank}. {player_name} - ${player_score}")
        rank += 1

def main():
    name = input("Enter your name: ")
    qs = [
        ("What is 2+2?", ["1", "2", "3", "4"], 4),
        ("Capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
        ("Python is a ...?", ["Snake", "Car", "Language", "Game"], 3)
    ]

    lifeline = True
    winnings = 0

    for i, (q, o, c) in enumerate(qs):
        correct, lifeline = ask(q, o, c, lifeline)
        if correct:
            winnings = prize(i)
            print(f"Correct! You now have ${winnings}\n")
        else:
            print("Wrong! Game over.")
            break
    else:
        winnings = prize(len(qs) - 1)
        print("Congratulations! You're a millionaire!")

    print(f"\n{name}'s final score: ${winnings}")
    save_score(name, winnings)

    all_scores = load_scores()
    show_top(all_scores)

if __name__ == "__main__":
    main()
