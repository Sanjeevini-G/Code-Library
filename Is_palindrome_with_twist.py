# Problem Statement:
# You are given a string s. Write a function that determines if the string is a palindrome, ignoring any non-alphanumeric characters. A palindrome is a string that reads the same backwards as forwards.

# Input Format:
# The input string s will have at most length 10^5. 
# The input string s will contain only printable ASCII characters.

# Constraints:
# 1 <= s <= 10^5.

# Output Format:
# The function should return True if s is a palindrome after ignoring any non-alphanumeric characters, and False otherwise.

# Sample Test Cases: 
# Input : 
# aaa
# Output:
# True

def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

s = input().strip()
result = is_palindrome(s)
print(result)


