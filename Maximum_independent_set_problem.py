def max_independent_set(weights):
    n = len(weights)
    if n == 0:
        return 0
    if n == 1:
        return weights[0]
    dp = [0] * n
    dp[0] = weights[0]
    dp[1] = max(weights[0], weights[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+weights[i])
    return dp[-1]

weights = list(map(int, input("Enter the weights of vertices: ").split()))
max_weight = max_independent_set(weights)
print("Maximum weight of independent set:", max_weight)
