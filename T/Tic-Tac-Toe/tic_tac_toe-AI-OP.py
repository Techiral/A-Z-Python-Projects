from tkinter import *
import numpy as np

size_of_board = 800
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'
Green_color = '#7BC043'


class Tic_Tac_Toe():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
        self.canvas.pack()
        # Input from the user in the form of clicks
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game-based objects on the canvas
    # ------------------------------------------------------------------

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
    def ai_make_move(self):
        if not self.gameover:
            if not self.player_X_turns:
                ai_move = self.ai_move()
                self.draw_O(ai_move)
                self.board_status[ai_move[0]][ai_move[1]] = 1
                self.player_X_turns = True
                self.is_gameover()
                
    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text = 'Winner: Player 1 (X)'
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = 'Winner: Player 2 (O)'
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = 'It\'s a tie'
            color = 'gray'

        self.canvas.delete("all")
        self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

        score_text = 'Scores \n'
        self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                text=score_text)

        score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
        score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
        score_text += 'Tie                    : ' + str(self.tie_score)
        self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                text=score_text)
        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                text=score_text)

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        if self.board_status[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def is_winner(self, player):
        player = -1 if player == 'X' else 1

        # Three in a row
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        # Diagonals
        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):
        r, c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True
        return tie

    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        gameover = self.X_wins or self.O_wins or self.tie
        return gameover

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns

                    if not self.is_gameover():
                        self.window.after(1000, self.ai_make_move)  # Delay AI's move

                    if self.is_gameover():
                        self.display_gameover()
                else:
                    print("Invalid move: Cell already occupied.")
        else:  # Play Again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


    def ai_move(self):
        best_score = -float("inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board_status[i][j] == 0:
                    self.board_status[i][j] = 1  # Simulate the AI (Player 2, 'O') making a move
                    score = self.minimax(self.board_status, 0, False)
                    self.board_status[i][j] = 0  # Undo the move

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            return best_move
        else:
            # Fallback: Choose the first available empty cell
            for i in range(3):
                for j in range(3):
                    if self.board_status[i][j] == 0:
                        return (i, j)

    def minimax(self, board, depth, is_maximizing):
        scores = {'X': -1, 'O': 1, 'tie': 0}

        result = self.check_winner()
        if result:
            return scores[result]

        if is_maximizing:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = 1  # Simulate Player 2 ('O') move
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = 0  # Undo the move
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 0:
                        board[i][j] = -1  # Simulate Player 1 ('X') move
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = 0  # Undo the move
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        # Check if Player 1 ('X') wins
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == -1:
                return 'X'
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == -1:
                return 'X'

        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == -1:
            return 'X'
        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == -1:
            return 'X'

        # Check if Player 2 ('O') wins
        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == 1:
                return 'O'
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == 1:
                return 'O'

        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == 1:
            return 'O'
        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == 1:
            return 'O'

        # Check if it's a tie
        for i in range(3):
            for j in range(3):
                if self.board_status[i][j] == 0:
                    return None
        return 'tie'

game_instance = Tic_Tac_Toe()
game_instance.mainloop()
