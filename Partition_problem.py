def findPartition(arr):
    n = len(arr)
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    half_sum = total_sum // 2
    dp = [[False] * (half_sum+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, half_sum+1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] |= dp[i-1][j-arr[i-1]]
    return dp[n][half_sum]

arr = [3, 1, 5, 9, 12]
print(findPartition(arr))  # Output: True
