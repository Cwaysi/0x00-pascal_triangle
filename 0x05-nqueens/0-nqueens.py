#!/usr/bin/python3
 """ solve"""
import sys

def is_safe(board, row, col, N):
    """ solve"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check for queens in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check for queens in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, N):
    """ solve"""
    if row == N:
        return [board[:]]
    
    solutions = []
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solutions += solve_nqueens_util(board, row + 1, N)
            board[row][col] = 0
    
    return solutions

def solve_nqueens(N):
     """ solve"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = solve_nqueens_util(board, 0, N)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    solve_nqueens(sys.argv[1])
