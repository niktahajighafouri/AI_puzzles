import math


def is_safe(board, row, col, N):
    # Check if the queen can be placed at board[row][col]
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def minimax(board, depth, is_max, alpha, beta, N):
    if depth == N:
        return evaluate(board, N)

    if is_max:
        max_eval = -math.inf
        for i in range(N):
            if is_safe(board, i, depth, N):
                board[i][depth] = 1
                eval = minimax(board, depth + 1, False, alpha, beta, N)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                board[i][depth] = 0
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(N):
            if is_safe(board, i, depth, N):
                board[i][depth] = 1
                eval = minimax(board, depth + 1, True, alpha, beta, N)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                board[i][depth] = 0
                if beta <= alpha:
                    break
        return min_eval


def evaluate(board, N):
    # A simple heuristic to evaluate the board
    # Here, it just counts the number of queens placed
    count = 0
    for i in range(N):
        for j in range(N):
            count += board[i][j]
    return count


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    minimax(board, 0, True, -math.inf, math.inf, N)
    print("Solution:")
    print_solution(board, N)


# Example usage:
n = 4  # Change this value to solve for a different N
solve_n_queens(n)

