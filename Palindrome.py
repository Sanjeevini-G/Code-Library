# Input string
s = "racecar"

# Function to check if a string is a palindrome
def isPalindrome(s):
    return s == s[::-1]

# Output
if isPalindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
