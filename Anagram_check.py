# Problem Statement:
# Given two strings, write a code to determine if they are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase. The function should take in two strings as input and return True if they are anagrams of each other, and False otherwise.

# Input Format:
# Two strings, string1 and string2, where 1 <= len(string1) <= 10^4 and 1 <= len(string2) <= 10^4.

# Constraints:
# The input strings will only contain lowercase and/or uppercase English letters, whitespace, and/or punctuation marks. 
# The input strings may contain leading or trailing whitespaces, which should be ignored when checking for anagrams. 

# Output Format:
# A boolean value indicating whether the two strings are anagrams of each other or not.

# Sample Test Cases: 
# Input : 
# Debit card
# Bad credit
# Output:
# True

def is_anagram(string1: str, string2: str) -> bool:
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    string1_sorted = sorted(string1)
    string2_sorted = sorted(string2)
    return string1_sorted == string2_sorted


if __name__ == "__main__":
    
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if is_anagram(string1, string2):
        print("The two strings are anagrams!")
    else:
        print("The two strings are not anagrams.")


