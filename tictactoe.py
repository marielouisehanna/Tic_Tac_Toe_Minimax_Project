
def check_winner(board):
    # Check rows and columns
    for i in range(4):
        if all(board[i][j] == 'X' for j in range(4)) or all(board[i][j] == 'O' for j in range(4)):
            return board[i][0]
        if all(board[j][i] == 'X' for j in range(4)) or all(board[j][i] == 'O' for j in range(4)):
            return board[0][i]

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(4)) or all(board[i][i] == 'O' for i in range(4)):
        return board[0][0]
    if all(board[i][3 - i] == 'X' for i in range(4)) or all(board[i][3 - i] == 'O' for i in range(4)):
        return board[0][3]

    # Check for tie
    if all(board[i][j] != '' for i in range(4) for j in range(4)):
        return "Tie"

    return None

def reset_board():
    return [['' for _ in range(4)] for _ in range(4)]

def player_move(board, buttons, row, col):
    if board[row][col] == '':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled', disabledforeground='#03DAC6')  # Light green for X's
        return True  # Move was successful
    return False  # Cell was already occupied
