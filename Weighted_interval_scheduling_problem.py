def latestNonConflict(interval, i):
    for j in range(i - 1, -1, -1):
        if interval[j][1] <= interval[i - 1][0]:
            return j
    return -1

def findMaxProfit(interval):
    n = len(interval)
    interval.sort(key=lambda x: x[1])
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        inclProf = interval[i - 1][2]
        prev = latestNonConflict(interval, i)
        if prev != -1:
            inclProf += dp[prev + 1]
        dp[i] = max(inclProf, dp[i - 1])

    return dp[n]

n = int(input("Enter the number of intervals: "))
interval = []
for i in range(n):
    start, end, profit = map(int, input(f"Enter interval {i + 1}: ").split())
    interval.append((start, end, profit))

print("Maximum profit:", findMaxProfit(interval))
