def is_valid(board, row, col, num):
    # Check if the number can be placed in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def find_empty_location(board):
    # Find an empty position in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def forward_checking(board, row, col, num, domains):
    # Update domains after placing a number
    for i in range(9):
        # Remove the number from the domain of the cells in the same row and column
        domains[row][i].discard(num)
        domains[i][col].discard(num)
        
        # Remove the number from the domain of the cells in the same 3x3 block
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        domains[box_row + i // 3][box_col + i % 3].discard(num)

def solve_sudoku(board):
    empty = find_empty_location(board)
    
    # If no empty position is found, the Sudoku is solved
    if not empty:
        return True
    
    row, col = empty

    # Try placing numbers 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number
            board[row][col] = num
            
            # Create a copy of the board to restore if needed
            board_copy = [row[:] for row in board]
            
            # Perform forward checking
            domains = [[set(range(1, 10)) for _ in range(9)] for _ in range(9)]
            forward_checking(board, row, col, num, domains)
            
            # Recursive call
            if solve_sudoku(board):
                return True
            
            # If the current placement leads to an invalid solution, backtrack
            board = board_copy
    
    # If no number can be placed, backtrack
    return False

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(sudoku_board)

# Print the solved Sudoku board
for row in sudoku_board:
    print(row)