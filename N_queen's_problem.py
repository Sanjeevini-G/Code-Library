def print_board(board):
    for row in board:
        print(' '.join(row))

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    def backtrack(col):
        nonlocal solutions
        if col == n:
            sol = []
            for row in board:
                sol.append(''.join(row))
            solutions.append(sol)
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'
    backtrack(0)
    return solutions

n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    print_board(solution)
    print()
