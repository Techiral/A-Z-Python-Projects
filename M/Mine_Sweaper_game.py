import random

# Define the game board
board_size = 10
num_mines = 10
board = [[0 for _ in range(board_size)] for _ in range(board_size)]

# Place the mines randomly on the board
mines = random.sample(range(board_size * board_size), num_mines)
for mine in mines:
    row = mine // board_size
    col = mine % board_size
    board[row][col] = -1

# Calculate the number of adjacent mines for each cell
for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == -1:
            continue
        for i in range(max(0, row - 1), min(board_size, row + 2)):
            for j in range(max(0, col - 1), min(board_size, col + 2)):
                if board[i][j] == -1:
                    board[row][col] += 1

# Define the game loop
while True:
    # Display the current board
    for row in board:
        print(' '.join(str(cell) for cell in row))

    # Prompt the player for input
    row = int(input('Enter row: '))
    col = int(input('Enter column: '))

    # Check if the player hit a mine
    if board[row][col] == -1:
        print('Game over!')
        break

    # Reveal the cell and check if the player won
    board[row][col] = -2
    if all(all(cell in (-1, -2) for cell in row) for row in board):
        print('You win!')
        break