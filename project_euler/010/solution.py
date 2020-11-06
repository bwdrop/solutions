#!/usr/bin/python3

def sum_of_sieve_under(nb):
    primes = [True for i in range(nb)]
    p = 2
    sum = 0
    while p * p <= nb:
        if primes[p]:
            sum += p
            for i in range(2 * p, nb, p):
                primes[i] = False
        p += 1
    # add primes > sqrt(nb) but under nb
    for i in range(p, nb):
        if primes[i]:
            sum += i
    return sum

print(sum_of_sieve_under(2000000))
