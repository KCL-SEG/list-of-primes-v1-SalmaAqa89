"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 2
    while len(list) < number_of_primes:
        isPrime = True
        for j in range (2, int(i**0.5) + 1):
            if i%j == 0:
                isPrime = False
        if isPrime:
            list.append(i)
        i += 1
    return list

print(primes(10))
