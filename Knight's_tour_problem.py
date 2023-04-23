def is_valid(x, y, board, n):
    if x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1:
        return True
    return False

def solve_knight_tour_util(board, n, move_x, move_y, x, y, pos):
    if pos == n*n:
        return True
    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if is_valid(new_x, new_y, board, n):
            board[new_x][new_y] = pos
            if solve_knight_tour_util(board, n, move_x, move_y, new_x, new_y, pos+1):
                return True
            board[new_x][new_y] = -1
    return False

def solve_knight_tour(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    board[0][0] = 0
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    if solve_knight_tour_util(board, n, move_x, move_y, 0, 0, 1):
        for row in board:
            print(row)
    else:
        print("Solution does not exist")

solve_knight_tour(8)  # Output: solution board for 8x8 board
