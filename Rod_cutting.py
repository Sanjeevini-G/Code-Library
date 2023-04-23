def rodCutting(lengths, prices, rodLength):
    n = len(lengths)
    dp = [[0] * (rodLength+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, rodLength+1):
            if lengths[i-1] <= j:
                dp[i][j] = max(prices[i-1] + dp[i][j-lengths[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][rodLength]

lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
rodLength = 4
print(rodCutting(lengths, prices, rodLength))  # Output: 10
