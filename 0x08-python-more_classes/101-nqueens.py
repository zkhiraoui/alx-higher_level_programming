"""Solves the N-queens puzzle.

This script finds all possible solutions for placing N non-attacking queens on an NxN chessboard, where N is a user-provided integer greater than or equal to 4.

Usage:
    Run the script with N as an argument, e.g., `./101-nqueens.py 4` for a 4x4 chessboard.

Attributes:
    board (list): Represents the chessboard as a list of lists. Initialized with spaces to denote empty squares.
    solutions (list): Accumulates the valid board configurations, each showing the positions of N queens.

Each solution is formatted as a list of [row, column] pairs, indicating where queens are placed on the board.
"""

import sys


def init_board(n):
    """Initializes an NxN chessboard filled with spaces to denote empty squares.

    Args:
        n (int): The size of the chessboard.

    Returns:
        A 2D list representing the chessboard.
    """
    return [[' ' for _ in range(n)] for _ in range(n)]


def board_deepcopy(board):
    """Creates a deep copy of the chessboard.

    Args:
        board (list): The chessboard to be copied.

    Returns:
        A new, independent copy of the chessboard.
    """
    return [row[:] for row in board]


def get_solution(board):
    """Extracts the queen positions from the chessboard.

    Args:
        board (list): A chessboard configuration with queens placed.

    Returns:
        A list of [row, column] pairs where queens are placed.
    """
    return [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]


def xout(board, row, col):
    """Marks squares where queens cannot be placed due to chess rules.

    Updates the board in-place, marking squares under attack from a queen placed at (row, col) with 'x'.

    Args:
        board (list): The chessboard.
        row (int): Row index of the newly placed queen.
        col (int): Column index of the newly placed queen.
    """
    n = len(board)
    for i in range(n):
        for j in range(n):
            if i == row or j == col or abs(row - i) == abs(col - j):
                if board[i][j] == ' ':
                    board[i][j] = 'x'


def recursive_solve(board, row, queens, solutions):
    """Recursively searches for all solutions to the N-queens puzzle.

    Args:
        board (list): The current chessboard.
        row (int): The current row being examined.
        queens (int): The number of queens placed so far.
        solutions (list): Accumulated solutions.

    Returns:
        The solutions list, updated with any new solutions found.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == ' ':
            new_board = board_deepcopy(board)
            new_board[row][col] = 'Q'
            xout(new_board, row, col)
            recursive_solve(new_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit() or int(N) < 4:
        print("N must be a number and at least 4")
        sys.exit(1)

    board = init_board(int(N))
    solutions = recursive_solve(board, 0, 0, [])
    for solution in solutions:
        print(solution)
