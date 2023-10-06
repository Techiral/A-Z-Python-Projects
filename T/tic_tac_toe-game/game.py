def print_board(board):
    # Print the game board with separators
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check if the player has won horizontally, vertically, or diagonally
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                # Get player input for row and column
                row, col = map(int, input("Enter row and column (e.g., 0 1): ").split())
                
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    # Update the board with the player's move
                    board[row][col] = current_player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter two numbers (e.g., 0 1).")
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif " " not in [cell for row in board for cell in row]:
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players for the next turn
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
