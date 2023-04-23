def longest_alternating_subarray(arr):
    n = len(arr)
    longest_len = 1
    curr_len = 1
    
    for i in range(1, n):
        if arr[i] * arr[i-1] < 0:
            curr_len += 1
            longest_len = max(longest_len, curr_len)
        else:
            curr_len = 1
    
    return longest_len
