def optimalStrategy(coins):
    n = len(coins)

    dp = [[0] * n for _ in range(n)]

    for gap in range(n):
        for i in range(n - gap):
            j = i + gap

            x = dp[i + 2][j] if (i + 2) <= j else 0
            y = dp[i + 1][j - 1] if (i + 1) <= (j - 1) else 0
            z = dp[i][j - 2] if i <= (j - 2) else 0

            dp[i][j] = max(coins[i] + min(x, y), coins[j] + min(y, z))

    return dp[0][n - 1]

n = int(input("Enter the number of coins: "))
coins = list(map(int, input("Enter the values of the coins: ").split()))

print("Maximum possible amount that can be collected:", optimalStrategy(coins))
