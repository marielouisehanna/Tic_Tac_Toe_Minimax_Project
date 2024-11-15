# evaluation_function.py
def evaluate(board):
    """
    Evaluate the board and return a score with differentiated offensive and defensive strategies.
    Positive scores favor 'X' (AI), and negative scores favor 'O' (human).
    """
    def score_line(line):
        x_count = line.count('X')
        o_count = line.count('O')
        if o_count == 0:  # Pure AI potential
            if x_count == 3:
                return 100  # Almost winning
            elif x_count == 2:
                return 10
            elif x_count == 1:
                return 1
        elif x_count == 0:  # Pure blocking human potential
            if o_count == 3:
                return -50  # Block human from winning
            elif o_count == 2:
                return -10
        return 0  # Mixed or empty lines have no immediate value

    score = 0
    # Check rows, columns, and both diagonals
    lines = []
    for i in range(4):
        lines.append(board[i])  # rows
        lines.append([board[j][i] for j in range(4)])  # columns

    lines.append([board[i][i] for i in range(4)])  # main diagonal
    lines.append([board[i][3-i] for i in range(4)])  # secondary diagonal

    for line in lines:
        score += score_line(line)

    return score
