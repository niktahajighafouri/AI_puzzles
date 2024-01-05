# Add necessary imports
from rich.console import Console
from rich.tree import Tree

console = Console()


# Function to display the chessboard
def display_board(board):
    for row in board:
        console.print(" ".join(row))


# Function to check if the current position is safe for the queen
def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


# Function to solve N-Queens using recursive backtracking
def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False


# Function to initialize and solve the N-Queens problem
def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        console.print("No solution exists for N = ", n)
        return
    display_board(board)


# Function to create and display the tree structure
def display_tree():
    tree = Tree("Initial State (Depth 0)")
    for i in range(1, 5):  # Example depth, change it as needed
        node = tree.add_node(f"Depth {i}")
        for j in range(4):  # Example branching factor, change it as needed
            node.add_node(f"({i},{j})")
    console.print(tree)


# Main function to display menu and handle user input
def main():
    while True:
        console.print("\nMenu:")
        console.print("1. Show Chessboard Preview")
        console.print("2. Show Tree")
        console.print("3. Solve N-Queens Problem")
        console.print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            n = int(input("Enter the number of queens: "))
            n_queens(n)
        elif choice == "2":
            display_tree()
        elif choice == "3":
            n = int(input("Enter the number of queens: "))
            n_queens(n)
        elif choice == "4":
            break
        else:
            console.print("Invalid choice. Please enter a valid option (1-4).")


if __name__ == "__main__":
    main()
