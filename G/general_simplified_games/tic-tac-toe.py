def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_win(board):
    # Check rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def main():
    board = [[' '] * 3 for _ in range(3)]
    current_player = 'X'

    for _ in range(9):
        print_board(board)
        while True:
            try:
                row, col = map(int, input(f"Player {current_player}, enter row and column (0, 1, 2) separated by space: ").split())
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
