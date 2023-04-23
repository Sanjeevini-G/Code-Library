def kadane(arr, start, end, n):
    max_so_far = float('-inf')
    max_ending_here = 0
    pos = start
    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end[0] = i
            start[0] = pos
        if max_ending_here < 0:
            max_ending_here = 0
            pos = i+1
    if end[0] == -1:
        end[0] = start[0]
    return max_so_far

def find_max_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    left, right, top, bottom = None, None, None, None
    start = [0]
    end = [0]
    for i in range(cols):
        temp = [0] * rows
        for j in range(i, cols):
            for k in range(rows):
                temp[k] += matrix[k][j]
            current_sum = kadane(temp, start, end, rows)
            if current_sum > max_sum:
                max_sum = current_sum
                left, right, top, bottom = i, j, start[0], end[0]
    return (max_sum, left, right, top, bottom)

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
print(find_max_sum(matrix))  # Output: (29, 1, 3, 1, 3)
