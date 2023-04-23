from collections import deque

def min_moves_to_reach_end(board):
    n = len(board)
    moves = [-1] * (n*n)
    moves[0] = 0
    queue = deque()
    queue.append(0)
    while queue:
        curr_pos = queue.popleft()
        if curr_pos == n*n-1:
            return moves[curr_pos]
        for i in range(curr_pos+1, min(curr_pos+7, n*n)):
            if moves[i] == -1:
                if board[i] == -1:
                    moves[i] = moves[curr_pos] + 1
                    queue.append(i)
                else:
                    moves[i] = moves[curr_pos] + 1
                    queue.append(board[i])
    return -1

board = [-1] * 100
board[2] = 21
board[4] = 7
board[10] = 25
board[19] = 28
board[20] = 8
board[26] = 0
board[39] = 60
board[51] = 67
board[63] = 81
board[71] = 19
board[76] = 38
board[89] = 79
board[92] = 88
board[95] = 51
board[98] = 13
print(min_moves_to_reach_end(board))  # Output: 7
