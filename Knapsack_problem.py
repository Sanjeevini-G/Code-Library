def knapsack_01(profits, weights, capacity):
    n = len(profits)
    dp = [[0] * (capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + profits[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][capacity]

n = int(input("Enter the number of items: "))
profits = list(map(int, input("Enter the profits of the items: ").split()))
weights = list(map(int, input("Enter the weights of the items: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))
max_profit = knapsack_01(profits, weights, capacity)
print("The maximum profit that can be obtained is:", max_profit)
