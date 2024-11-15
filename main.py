import tkinter as tk
import tictactoe
import opponents

# Initialize the game window
window = tk.Tk()
window.title("Tic-Tac-Toe 4x4")
window.geometry("500x600")
window.configure(bg='#121212')  # Dark background

# Variables to store board and opponent type
board = tictactoe.reset_board()
opponent_type = tk.StringVar(value="Random Opponent")  # Default opponent

# Create the board (4x4 grid)
board_frame = tk.Frame(window, bg='#121212')
board_frame.place(relx=0.5, rely=0.4, anchor='center')

# Initialize the grid of buttons
buttons = [[None for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        buttons[i][j] = tk.Button(
            board_frame, text='', font=('Arial', 20), width=5, height=2,
            bg='#2E2E2E', fg='white', activebackground='#f44336',
            activeforeground='white', borderwidth=0, relief='flat',
            highlightthickness=0, padx=10, pady=5, bd=0,
            command=lambda row=i, col=j: player_move(row, col)
        )
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j].config(highlightbackground='#2E2E2E', highlightcolor='#2E2E2E', relief='flat')

# Function to handle player's move
def player_move(row, col):
    if tictactoe.player_move(board, buttons, row, col):
        winner = tictactoe.check_winner(board)
        if winner:
            end_game(winner)
        else:
            opponent_move()

# Function to handle opponent's move
# def opponent_move():
#     if opponent_type.get() == "Random Opponent":
#         winner = opponents.random_opponent_move(board, buttons)
#         if winner:
#             end_game(winner)
#     else:
#         # Placeholder for future opponent types
#         result_label.config(text=f"{opponent_type.get()} not available!", fg='#f44336')

# Function to handle opponent's move
def opponent_move():
    opponent = opponent_type.get()
    if opponent == "Random Opponent":
        winner = opponents.random_opponent_move(board, buttons)
    else:
        winner = opponents.minimax_opponent_move(board, buttons, opponent)
    
    if winner:
        end_game(winner)



# Function to end the game
def end_game(winner):
    if winner == "Tie":
        result_label.config(text="It's a Tie!", fg='#f44336')
    else:
        result_label.config(text=f'{winner} wins!', fg='#f44336')
    # Disable all buttons
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(state='disabled')

# Function to reset the game
def reset_game():
    global board
    board = tictactoe.reset_board()
    for i in range(4):
        for j in range(4):
            buttons[i][j].config(text='', state='normal')
    result_label.config(text="")

# Opponent selection buttons
control_frame = tk.Frame(window, bg='#121212')
control_frame.place(relx=0.5, rely=0.8, anchor='center')


def select_opponent(opponent):
    opponent_type.set(opponent)
    result_label.config(text=f"{opponent} selected!", fg='#03DAC6')


button_style = {
    'font': ('Arial', 14), 'bg': '#2E2E2E', 'fg': 'white',
    'activebackground': '#f44336', 'activeforeground': 'white',
    'borderwidth': 0, 'padx': 15, 'pady': 5, 'relief': 'flat'
}

# Opponent buttons
easy_button = tk.Button(control_frame, text="Easy", command=lambda: select_opponent("Easy"), **button_style)
easy_button.grid(row=0, column=0, padx=10)

medium_button = tk.Button(control_frame, text="Medium", command=lambda: select_opponent("Medium"), **button_style)
medium_button.grid(row=0, column=1, padx=10)

hard_button = tk.Button(control_frame, text="Hard", command=lambda: select_opponent("Hard"), **button_style)
hard_button.grid(row=0, column=2, padx=10)

random_button = tk.Button(control_frame, text="Random", command=lambda: select_opponent("Random Opponent"), **button_style)
random_button.grid(row=0, column=3, padx=10)

# Result label
result_label = tk.Label(window, text="", font=('Arial', 18), bg='#121212', fg='white')
result_label.place(relx=0.5, rely=0.9, anchor='center')

# Reset button
reset_button = tk.Button(
    window, text="Reset Game", font=('Arial', 14), bg='#2E2E2E', fg='white',
    activebackground='#f44336', activeforeground='white', command=reset_game,
    borderwidth=0, padx=10, pady=5, relief='flat'
)
reset_button.place(relx=0.5, rely=0.95, anchor='center')

# Start the GUI event loop
window.mainloop()
