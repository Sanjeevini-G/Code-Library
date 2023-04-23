def longestConsecutive(arr):
    n = len(arr)
    s = set()
    ans = 0

    for i in range(n):
        s.add(arr[i])

    for i in range(n):
        if (arr[i] - 1) not in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans, j - arr[i])

    return ans

n = int(input("Enter the length of the array: "))
arr = list(map(int, input("Enter the array: ").split()))

print("Length of the longest consecutive subsequence:", longestConsecutive(arr))
