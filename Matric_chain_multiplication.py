def matrixChainMultiplication(p):
    n = len(p) - 1
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1])
    return dp[0][n-1]

p = [10, 20, 30, 40, 50]
print(matrixChainMultiplication(p))  # Output: 35000
