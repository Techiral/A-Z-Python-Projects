import random
import os
import time

# Constants
GRID_SIZE = 3
MOLE_CHAR = "M"
EMPTY_CHAR = "."
TIME_LIMIT = 30  # Time limit in seconds

# Initialize the grid
grid = [[EMPTY_CHAR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to display the grid
def display_grid():
    os.system("clear" if os.name == "posix" else "cls")
    for row in grid:
        print(" ".join(row))
    print("\nTime left: {} seconds".format(time_left))

# Function to place a mole randomly
def place_mole():
    row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    grid[row][col] = MOLE_CHAR

# Main game loop
start_time = time.time()
time_left = TIME_LIMIT

while time_left > 0:
    display_grid()
    place_mole()
    
    try:
        row, col = map(int, input("Whack the mole (row col): ").split())
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            if grid[row][col] == MOLE_CHAR:
                grid[row][col] = EMPTY_CHAR
                time_left += 1  # Give the player extra time for a successful hit
    except (ValueError, IndexError):
        pass

    elapsed_time = time.time() - start_time
    time_left = TIME_LIMIT - int(elapsed_time)

display_grid()
print("Time's up! Game over.")
