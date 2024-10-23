# A utility function to check if there are moves remaining on the board
def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

# This is the evaluation function that gives a score to a terminal state
def evaluate(board):
    # Checking rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    # Checking columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Checking diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != '_':
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0] != '_':
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # If none of them have won, return 0
    return 0

# Alpha-Beta Pruning implementation for minimax
def alpha_beta(board, depth, is_maximizer, alpha, beta):
    score = evaluate(board)

    # If the maximizer or minimizer has won, return the score
    if score == 10 or score == -10:
        return score

    # If there are no more moves and no winner, it's a tie
    if not is_moves_left(board):
        return 0

    # Maximizing player (X)
    if is_maximizer:
        best = -float('inf')

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if the cell is empty
                if board[i][j] == '_':
                    # Make the move
                    board[i][j] = 'X'

                    # Call alpha_beta recursively and choose the maximum value
                    best = max(best, alpha_beta(board, depth + 1, False, alpha, beta))

                    # Undo the move
                    board[i][j] = '_'

                    # Alpha-Beta Pruning
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
        return best

    # Minimizing player (O)
    else:
        best = float('inf')

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if the cell is empty
                if board[i][j] == '_':
                    # Make the move
                    board[i][j] = 'O'

                    # Call alpha_beta recursively and choose the minimum value
                    best = min(best, alpha_beta(board, depth + 1, True, alpha, beta))

                    # Undo the move
                    board[i][j] = '_'

                    # Alpha-Beta Pruning
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
        return best

# Driver code for alpha-beta search
def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)

    # Traverse all cells, evaluate minimax function for all empty cells
    for i in range(3):
        for j in range(3):
            # Check if cell is empty
            if board[i][j] == '_':
                # Make the move
                board[i][j] = 'X'

                # Compute evaluation function for this move
                move_val = alpha_beta(board, 0, False, -float('inf'), float('inf'))

                # Undo the move
                board[i][j] = '_'

                # If the value of the current move is better than the best value, update best move
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example Tic-Tac-Toe board
board = [
    ['X', 'O', 'X'],
    ['_', 'O', '_'],
    ['_', '_', '_']
]

best_move = find_best_move(board)
print(f"The best move for 'X' is at position {best_move}")
