import math
from rich.console import Console

console = Console()


def is_safe(board, row, col, N):
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


def display_board(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                console.print("[green]Q[/green] ", end=" ")
            else:
                console.print("[white].[/white] ", end=" ")
        console.print()


def print_tree(board, depth, N):
    if depth == N:
        display_board(board, N)
        return

    for i in range(N):
        if is_safe(board, i, depth, N):
            board[i][depth] = 1
            print_tree(board, depth + 1, N)
            board[i][depth] = 0


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
    count = 0
    for i in range(N):
        for j in range(N):
            count += board[i][j]
    return count


def print_tree_structure(board, N):
    console.print("\nTree Structure:")
    print_tree(board, 0, N)


def main():
    N = int(console.input("Enter the size of the board (N): "))
    board = [[0 for _ in range(N)] for _ in range(N)]

    while True:
        console.print("\nMenu:")
        console.print("[bold cyan]1.[/bold cyan] Show Chessboard Preview")
        console.print("[bold cyan]2.[/bold cyan] Show Tree")
        console.print("[bold cyan]3.[/bold cyan] Solve N-Queens Problem")
        console.print("[bold cyan]4.[/bold cyan] See Base Example")
        console.print("[bold cyan]5.[/bold cyan] Exit")

        choice = int(console.input("\nEnter your choice: "))

        if choice == 1:
            console.print("\nChessboard Preview:")
            display_board(board, N)
        elif choice == 2:
            print_tree_structure(board, N)
        elif choice == 3:
            console.print("\nSolving N-Queens Problem...")
            minimax(board, 0, True, -math.inf, math.inf, N)
            console.print("\nSolution:")
            display_board(board, N)
        elif choice == 4:
            # Show a base example (e.g., 4x4 chessboard)
            base_board = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
            console.print("\nBase Example:")
            display_board(base_board, 4)
        elif choice == 5:
            console.print("Exiting... Goodbye!")
            break
        else:
            console.print("[bold red]Invalid choice. Please enter a valid option.[/bold red]")


if __name__ == "__main__":
    main()
