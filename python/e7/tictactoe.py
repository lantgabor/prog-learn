# tic_tac_toe.py
# A simple 2-player Tic Tac Toe game for beginners

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    # Create empty 3x3 board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Players take turns placing X and O on the board (row and column 1-3).")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get move from user
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter col (1-3): ")) - 1

        # Check if move is valid
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That spot is already taken. Try again.")
            continue

        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

if __name__ == "__main__":
    main()
