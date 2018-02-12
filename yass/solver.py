
"""
YASS - Yet Another Sudoku Solver
"""

from copy import deepcopy


ROWS = COLS = tuple(range(9))   # Row and column indices
SQUARES = (0, 3, 6)             # Indices of top-left corners of squares
COMPLETE = set(range(1, 10))    # Set of all numbers from 1 to 9 (a complete line, row or square)


def solve(board):
    """
    Solve a sudoku puzzle

    :param board: A 9 x 9 list of lists representing the sudoku board. Unknowns are represented by zeros.
    :return: The solution (a 9 x 9 list of lists) or None when impossible

    Example:

    >>> test = [
    ... [0, 0, 0, 2, 0, 0, 0, 1, 0],
    ... [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ... [8, 0, 6, 0, 0, 0, 0, 0, 0],
    ... [0, 7, 1, 0, 8, 4, 0, 9, 0],
    ... [0, 5, 0, 0, 0, 2, 3, 7, 0],
    ... [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ... [0, 0, 0, 7, 1, 0, 0, 6, 4],
    ... [0, 2, 0, 0, 0, 5, 0, 0, 0],
    ... [3, 0, 0, 4, 0, 0, 0, 0, 9]]
    >>> for row in solve(test):
    ...     print(row)
    [7, 3, 5, 2, 4, 8, 9, 1, 6]
    [1, 9, 2, 6, 3, 7, 4, 5, 8]
    [8, 4, 6, 1, 5, 9, 7, 2, 3]
    [2, 7, 1, 3, 8, 4, 6, 9, 5]
    [4, 5, 8, 9, 6, 2, 3, 7, 1]
    [9, 6, 3, 5, 7, 1, 8, 4, 2]
    [5, 8, 9, 7, 1, 3, 2, 6, 4]
    [6, 2, 4, 8, 9, 5, 1, 3, 7]
    [3, 1, 7, 4, 2, 6, 5, 8, 9]
    """

    # Sets of known numbers by row, column and square
    row_sets = [set(board[r]) for r in ROWS]
    col_sets = [set(board[r][c] for r in ROWS) for c in COLS]
    sqr_sets = [[set(board[rr][cc] for rr in range(r, r+3) for cc in range(c, c+3)) for c in SQUARES] for r in SQUARES]

    # If complete, return the board
    if all(s == COMPLETE for s in row_sets) and \
       all(s == COMPLETE for s in col_sets) and \
       all(s == COMPLETE for t in sqr_sets for s in t):
        return board

    # Select the empty cell (row, col) with the minimum number of options
    min_option_count = 10
    selected_cell_options = ()
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 0:
                options = COMPLETE - row_sets[r] - col_sets[c] - sqr_sets[r//3][c//3]
                if len(options) < min_option_count:
                    min_option_count = len(options)
                    selected_row, selected_col = r, c
                    selected_cell_options = options

    # Try every option in the selected cell
    for option in selected_cell_options:
        attempt = deepcopy(board)
        attempt[selected_row][selected_col] = option
        solution = solve(attempt)
        if solution is not None:
            return solution
