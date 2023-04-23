def longestRepeatedSubsequence(str):
    n = len(str)
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and str[i-1] == str[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    index = dp[n][n]
    lrs = [""] * (index+1)
    lrs[index] = "\0"
    i, j = n, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + 1:
            lrs[index-1] = str[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    return "".join(lrs[:-1])
