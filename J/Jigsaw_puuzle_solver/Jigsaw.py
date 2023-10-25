import cv2
import numpy as np

# Load the jigsaw puzzle pieces as images
piece1 = cv2.imread('piece1.jpg')
piece2 = cv2.imread('piece2.jpg')
# Add more pieces as needed

# Function to match and align two puzzle pieces
def match_pieces(piece1, piece2):
    # Your matching and alignment logic here
    # You can use features like keypoints and descriptors for matching

    # Example: Simple matching by resizing and rotating
    height, width, _ = piece1.shape
    piece2 = cv2.resize(piece2, (width, height))
    result = cv2.addWeighted(piece1, 0.5, piece2, 0.5, 0)
    
    return result

# Arrange puzzle pieces
def solve_puzzle(pieces):
    # Initial piece placement (e.g., top-left corner)
    solved_puzzle = pieces[0]

    for i in range(1, len(pieces)):
        # Match the current piece with the solved puzzle
        matched_piece = match_pieces(solved_puzzle, pieces[i])

        # Update the solved puzzle with the matched piece
        solved_puzzle = matched_piece

    return solved_puzzle

# List of puzzle pieces (add more pieces as needed)
puzzle_pieces = [piece1, piece2]

# Solve the puzzle
completed_puzzle = solve_puzzle(puzzle_pieces)

# Display the completed puzzle
cv2.imshow('Completed Puzzle', completed_puzzle)
cv2.waitKey(0)
cv2.destroyAllWindows()
