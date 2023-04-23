def shortestCommonSupersequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    index = dp[m][n]
    scs = [""] * (index+1)
    scs[index] = "\0"
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            scs[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            scs[index-1] = str2[j-1]
            j -= 1
            index -= 1
        else:
            scs[index-1] = str1[i-1]
            i -= 1
            index -= 1
    while i > 0:
        scs[index-1] = str1[i-1]
        i -= 1
        index -= 1
    while j > 0:
        scs[index-1] = str2[j-1]
        j -= 1
        index -= 1
    return "".join(scs[:-1])
