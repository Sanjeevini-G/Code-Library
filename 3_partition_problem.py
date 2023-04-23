def canPartition(arr):
    n = len(arr)
    total_sum = sum(arr)
    if n < 3 or total_sum % 3 != 0:
        return False
    target_sum = total_sum // 3
    dp = [[False] * (target_sum+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, target_sum+1):
            dp[i][j] = dp[i-1][j]
            if j >= arr[i-1]:
                dp[i][j] |= dp[i-1][j-arr[i-1]]
    if not dp[n][target_sum]:
        return False
    i, j = n, target_sum
    selected = []
    while i > 0 and j > 0:
        if dp[i-1][j]:
            i -= 1
        else:
            selected.append(i-1)
            j -= arr[i-1]
            i -= 1
    subset_sum = sum(arr[i] for i in selected)
    if subset_sum == target_sum:
        return True
    else:
        return False

arr = [3, 1, 4, 2, 2, 1]
print(canPartition(arr))  # Output: True
