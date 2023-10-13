# Text-Based Whack-a-Mole Game

This is a simple text-based Whack-a-Mole game implemented in Python. In this game, you have to "whack" moles that randomly appear on a grid within a time limit. Your goal is to score as many points as possible by hitting the moles within the given time.

## Prerequisites

Before you can run this game, ensure you have Python installed on your system. No external libraries are required for this text-based game.

## How to Play

1. Run the game by executing the Python script, `whack_a_mole.py`.
2. You will see a grid where moles (represented as 'M') will randomly pop up.
3. Whack the moles by inputting the row and column numbers (0-indexed) separated by a space.
4. If you successfully whack a mole, you earn extra time.
5. The game ends when the time runs out.

## Controls

- Use your keyboard to input the row and column numbers for whacking moles.

## Game Configuration

You can customize the game by modifying the following variables in the code:
- `GRID_SIZE`: Adjust the size of the grid.
- `MOLE_CHAR` and `EMPTY_CHAR`: You can change the characters used to represent moles and empty cells.
- `TIME_LIMIT`: Set the duration of the game in seconds.

## Author

- Harsh

Feel free to modify, enhance, or extend the game as you wish. Have fun playing!

**Note:** If you want a graphical version of Whack-a-Mole, consider using the Pygame library and explore available resources for building graphical games.

## Acknowledgments

This game was created as a simple Python project for entertainment and educational purposes. No moles were harmed in the making of this game.
