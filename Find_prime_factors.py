def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1
    return factors

# Example usage of prime_factors
n = 84
result = prime_factors(n)
print(result)    # prints [2, 2, 3, 7]
