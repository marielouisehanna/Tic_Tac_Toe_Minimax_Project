import math
from evaluation_function import evaluate

def minimax(board, depth, alpha, beta, is_maximizing, limit):
    winner = check_winner(board)
    if winner:
        return score(winner, depth)
    if is_full(board) or depth == limit:
        return evaluate(board)

    moves = get_all_possible_moves(board, is_maximizing)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(4):  
            for j in range(4):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, False, limit)
                    board[i][j] = ''
                    if eval > max_eval:
                        max_eval = eval
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, True, limit)
                    board[i][j] = ''
                    if eval < min_eval:
                        min_eval = eval
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

    # if is_maximizing:
    #     value = -math.inf
    #     for move in moves:
    #         board[move[0]][move[1]] = 'X'
    #         value = max(value, minimax(board, depth + 1, alpha, beta, False, limit))
    #         board[move[0]][move[1]] = ''
    #         alpha = max(alpha, value)
    #         if alpha >= beta:
    #             break
    #     return value
    # else:
    #     value = math.inf
    #     for move in moves:
    #         board[move[0]][move[1]] = 'O'
    #         value = min(value, minimax(board, depth + 1, alpha, beta, True, limit))
    #         board[move[0]][move[1]] = ''
    #         beta = min(beta, value)
    #         if beta <= alpha:
    #             break
    #     return value

def get_all_possible_moves(board, is_maximizing):
    moves = [(i, j) for i in range(4) for j in range(4) if board[i][j] == '']
    # Here we could sort moves based on some heuristic if desired
    return moves


def score(winner, depth):
    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    else:
        return 0

def best_move(board, limit):
    best_score = -math.inf
    move = None
    for i in range(4):
        for j in range(4):
            if board[i][j] == '':
                board[i][j] = 'X'
                score = minimax(board, 0, -math.inf, math.inf, False, limit)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def is_full(board):
    return all(all(cell != '' for cell in row) for row in board)

def check_winner(board):
    for i in range(4):
        if all(board[i][j] == 'X' for j in range(4)) or all(board[i][j] == 'O' for j in range(4)):
            return board[i][0]
        if all(board[j][i] == 'X' for j in range(4)) or all(board[j][i] == 'O' for j in range(4)):
            return board[0][i]

    if all(board[i][i] == 'X' for i in range(4)) or all(board[i][i] == 'O' for i in range(4)):
        return board[0][0]
    if all(board[i][3 - i] == 'X' for i in range(4)) or all(board[i][3 - i] == 'O' for i in range(4)):
        return board[0][3]

    if all(board[i][j] != '' for i in range(4) for j in range(4)):
        return "Tie"

    return None
