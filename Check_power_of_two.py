def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n-1)) == 0

# Example usage of is_power_of_two
print(is_power_of_two(8))    # prints True
print(is_power_of_two(10))   # prints False
