def generatePrimes(n):
    primes = []
    isPrime = [True] * (n+1)
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, n+1):
        if isPrime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    
    return primes
