import math
from rich.console import Console
from rich.table import Table

console = Console()


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


def display_board(board, N):
    table = Table(title="Chessboard Preview")
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i][j] == 1:
                row += "[green]Q[/green] "
            else:
                row += "[white].[/white] "
        table.add_row(row)
    console.print(table)


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


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    minimax(board, 0, True, -math.inf, math.inf, N)
    display_board(board, N)


def display_tree_levels(N, depth):
    board = [[0 for _ in range(N)] for _ in range(N)]
    console.print("\nTree Levels:")
    console.print("Initial State (Depth 0):")
    display_board(board, N)
    for i in range(depth):
        if i % 2 == 0:
            console.print(f"\n[bold green]Max's turn (Depth {i + 1}):[/bold green]")
        else:
            console.print(f"\n[bold red]Min's turn (Depth {i + 1}):[/bold red]")
        minimax(board, i, i % 2 == 0, -math.inf, math.inf, N)
        display_board(board, N)


def print_menu():
    console.print("\nMenu:")
    console.print("[bold cyan]1.[/bold cyan] Show Chessboard Preview")
    console.print("[bold cyan]2.[/bold cyan] Show Tree (First Few Levels)")
    console.print("[bold cyan]3.[/bold cyan] Solve N-Queens Problem")
    console.print("[bold cyan]4.[/bold cyan] Show Default Example")
    console.print("[bold cyan]5.[/bold cyan] Enter Custom Input")
    console.print("[bold cyan]6.[/bold cyan] Exit")


def get_user_choice():
    return int(console.input("\nEnter your choice: "))


def get_custom_input():
    size = int(console.input("\nEnter the size of the board (N): "))
    return size


def default_example():
    n = 4
    console.print("\nDefault Example (N = 4):")
    solve_n_queens(n)


def main():
    console.print("N-Queens Problem using Minimax Algorithm with Alpha-Beta Pruning")
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            display_board([[0 for _ in range(4)] for _ in range(4)], 4)
        elif choice == 2:
            depth = 4  # Show first few levels of the tree (adjust depth as needed)
            display_tree_levels(4, depth)
        elif choice == 3:
            N = 4  # Change this value to solve for a different N
            console.print("\nSolving N-Queens Problem...")
            solve_n_queens(N)
        elif choice == 4:
            default_example()
        elif choice == 5:
            custom_input = get_custom_input()
            console.print(f"\nCustom Input (N = {custom_input}):")
            solve_n_queens(custom_input)
        elif choice == 6:
            console.print("Exiting... Goodbye!")
            break
        else:
            console.print("[bold red]Invalid choice. Please enter a valid option.[/bold red]")


if __name__ == "__main__":
    main()
