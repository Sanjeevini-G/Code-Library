def LAS(arr):
    n = len(arr)

    inc = [1] * n
    dec = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], dec[j] + 1)
            elif arr[i] < arr[j]:
                dec[i] = max(dec[i], inc[j] + 1)

    return max(inc + dec) - 1

n = int(input("Enter the length of the array: "))
arr = list(map(int, input("Enter the array: ").split()))

print("Length of the longest alternating subsequence:", LAS(arr))
