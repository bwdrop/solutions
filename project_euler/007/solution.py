#!/usr/bin/python3

def check_if_prime(nb, primes):
    for p in primes:
        if nb % p == 0:
            return False
    return True

def get_nth_prime(n):
    primes = [2]
    p = 3
    while len(primes) < n:
        if check_if_prime(p, primes):
            primes.append(p)
        p += 2
    return primes.pop()

print(get_nth_prime(10001))
