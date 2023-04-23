def longest_palindrome(s):
    n = len(s)
    max_len = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if s[i + k] != s[j - k]:
                    flag = 0
                    break
            if flag != 0 and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1
    return s[start:start + max_len]

s = "babad"
print(longest_palindrome(s))  # Output: "bab"

s = "cbbd"
print(longest_palindrome(s))  # Output: "bb"
