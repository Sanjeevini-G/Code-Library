def is_leap_year(year):
    # Leap year is divisible by 4 and not divisible by 100 or is divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Example usage of is_leap_year
year = 2024
result = is_leap_year(year)
print(result)    # prints True
