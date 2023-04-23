def largest_consecutive_subarray(arr):
    n = len(arr)
    max_len = 0
    start = 0
    for i in range(n):
        if i < n-1 and arr[i+1] == arr[i]+1:
            continue
        if i-start+1 > max_len:
            max_len = i-start+1
            end = i
        start = i+1
    return arr[end-max_len+1:end+1]

arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(largest_consecutive_subarray(arr))  # Output: [1, 2, 3, 4, 5, 6]
