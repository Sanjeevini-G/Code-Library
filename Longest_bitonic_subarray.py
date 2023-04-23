def bitonic(arr):
    n = len(arr)
    inc = [1] * n
    dec = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + 1)

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + 1)

    max_len = inc[0] + dec[0] - 1
    for i in range(1, n):
        curr_len = inc[i] + dec[i] - 1
        max_len = max(max_len, curr_len)

    return max_len

n = int(input("Enter the length of the array: "))
arr = list(map(int, input("Enter the array: ").split()))

print("Length of the longest bitonic subarray:", bitonic(arr))
