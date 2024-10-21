import tkinter as tk
import random

# Initialize the game window
window = tk.Tk()
window.title("Tic-Tac-Toe 4x4")
window.geometry("500x600")

# Dark vibes for the background
window.configure(bg='#121212')  # Dark greyish-black background

# Variables to store board and opponent type
board = [['' for _ in range(4)] for _ in range(4)]
opponent_type = tk.StringVar(value="Random Opponent")  # Default opponent

# Function to check for winner in a 4x4 grid
def check_winner():
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

# Random opponent logic
def random_opponent_move():
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state='disabled', disabledforeground='#f44336')  # Red for O's

        winner = check_winner()
        if winner:
            end_game(winner)

# Function to choose the opponent and execute its move
def opponent_move():
    if opponent_type.get() == "Random Opponent":
        random_opponent_move()
    # Future opponents can be added here with different logic

# Handle player's move
def player_move(row, col):
    if board[row][col] == '':
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled', disabledforeground='#03DAC6')  # Light green for X's

        winner = check_winner()
        if winner:
            end_game(winner)
        else:
            opponent_move()

# End game with a message
def end_game(winner):
    if winner == "Tie":
        result_label.config(text="It's a Tie!", fg='#f44336')  # Red for tie
    else:
        result_label.config(text=f'{winner} wins!', fg='#f44336')  # Red for winner

    # Disable all buttons
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(state='disabled')

# Reset the game
def reset_game():
    global board
    board = [['' for _ in range(4)] for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(text='', state='normal')
    
    result_label.config(text="")

# Create the board (4x4 grid) and opponent selector
board_frame = tk.Frame(window, bg='#121212')  # Dark vibes background for the board
board_frame.place(relx=0.5, rely=0.4, anchor='center')

# Initialize the grid of buttons with rounded corners
buttons = [[None for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        buttons[i][j] = tk.Button(board_frame, text='', font=('Arial', 20), width=5, height=2,
                                  bg='#2E2E2E', fg='white', activebackground='#f44336',  # Active red for Instagram vibe
                                  activeforeground='white', borderwidth=0, relief='flat',
                                  highlightthickness=0, padx=10, pady=5, bd=0,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j].config(highlightbackground='#2E2E2E', highlightcolor='#2E2E2E', relief='flat')

# Add opponent selection buttons (Easy, Medium, Hard, Random)
control_frame = tk.Frame(window, bg='#121212')  # Dark vibes background for the control buttons
control_frame.place(relx=0.5, rely=0.8, anchor='center')

def select_opponent(opponent):
    if opponent == "Random Opponent":
        opponent_type.set(opponent)
        result_label.config(text=f"{opponent} selected!", fg='#03DAC6')  # Green text for selected random opponent
    else:
        result_label.config(text=f"{opponent} not available!", fg='#f44336')  # Red for unavailable modes

# Button styles for dark theme
button_style = {'font': ('Arial', 14), 'bg': '#2E2E2E', 'fg': 'white', 'activebackground': '#f44336',
                'activeforeground': 'white', 'borderwidth': 0, 'padx': 15, 'pady': 5, 'relief': 'flat'}

# Easy button (non-functional)
easy_button = tk.Button(control_frame, text="Easy", command=lambda: select_opponent("Easy"), **button_style)
easy_button.grid(row=0, column=0, padx=10)

# Medium button (non-functional)
medium_button = tk.Button(control_frame, text="Medium", command=lambda: select_opponent("Medium"), **button_style)
medium_button.grid(row=0, column=1, padx=10)

# Hard button (non-functional)
hard_button = tk.Button(control_frame, text="Hard", command=lambda: select_opponent("Hard"), **button_style)
hard_button.grid(row=0, column=2, padx=10)

# Random button (functional)
random_button = tk.Button(control_frame, text="Random", command=lambda: select_opponent("Random Opponent"), **button_style)
random_button.grid(row=0, column=3, padx=10)

# Result label for game outcome
result_label = tk.Label(window, text="", font=('Arial', 18), bg='#121212', fg='white')
result_label.place(relx=0.5, rely=0.9, anchor='center')

# Reset button
reset_button = tk.Button(window, text="Reset Game", font=('Arial', 14), bg='#2E2E2E', fg='white', 
                         activebackground='#f44336', activeforeground='white', command=reset_game,
                         borderwidth=0, padx=10, pady=5, relief='flat')
reset_button.place(relx=0.5, rely=0.95, anchor='center')

# Start the GUI event loop
window.mainloop()
