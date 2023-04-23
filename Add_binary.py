class Solution(object):
    def addBinary(self, a, b):
        # Initialize variables for sum and carry
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Iterate through both strings in reverse
        while i >= 0 or j >= 0 or carry:
            # Get the digits to be added, or 0 if either string is finished
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum and carry
            digit_sum = digit_a + digit_b + carry
            carry = digit_sum // 2
            digit_sum %= 2
            
            # Add the current digit to the result string
            result = str(digit_sum) + result
            
            # Move to the next digits in both strings
            i -= 1
            j -= 1
            
        return result
