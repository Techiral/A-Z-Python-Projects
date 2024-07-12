import random

def create_board(size):
    return [["O" for _ in range(size)] for _ in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

def play_battleship():
    board_size = 5
    num_ships = 1

    print("Welcome to Battleship!")
    print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(4):
        print(f"Turn {turn + 1}")
        guess_row = int(input("Guess Row (0-4): "))
        guess_col = int(input("Guess Col (0-4): "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
        print_board(board)

if __name__ == "__main__":
    play_battleship()
