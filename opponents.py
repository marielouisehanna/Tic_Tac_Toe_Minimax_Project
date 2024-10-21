

import random
import tictactoe

def random_opponent_move(board, buttons):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state='disabled', disabledforeground='#f44336')  # Red for O's
        winner = tictactoe.check_winner(board)
        return winner
    return None  # No empty cells, game is a tie
