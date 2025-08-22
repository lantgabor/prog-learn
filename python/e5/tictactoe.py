# tic_tac_toe.py — simplest 2-player CLI

def draw(b):
    print(
        f"\n {b[0]} | {b[1]} | {b[2]}\n---+---+---\n {b[3]} | {b[4]} | {b[5]}\n---+---+---\n {b[6]} | {b[7]} | {b[8]}\n"
    )

def winning_lines(n):
    lines = []
    # rows
    for r in range(n):
        lines.append([(r, c) for c in range(n)])
    # cols
    for c in range(n):
        lines.append([(r, c) for r in range(n)])
    # diagonals
    lines.append([(i, i) for i in range(n)])
    lines.append([(i, n-1-i) for i in range(n)])
    return lines


def winner(board):
    n = len(board)
    for line in winning_lines(n):
        values = [board[r][c] for r, c in line]
        if values.count(values[0]) == n and values[0] in ("X", "O"):
            return values[0]
    return None


def play():
    b = [str(i + 1) for i in range(9)]
    turn = "X"
    for _ in range(9):
        draw(b)
        move = input(f"{turn} move (1-9): ").strip()
        if move not in [str(i) for i in range(1, 10)]:
            print("Invalid. Try 1-9.")
            continue
        i = int(move) - 1
        if b[i] in "XO":
            print("Occupied. Choose another.")
            continue
        b[i] = turn
        w = winner(b)
        if w:
            draw(b)
            print(f"{w} wins!")
            return
        turn = "O" if turn == "X" else "X"
    draw(b)
    print("Draw.")


if __name__ == "__main__":
    play()
