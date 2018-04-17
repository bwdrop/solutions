#!/usr/bin/python3

from math import sqrt

def get_prime_factors(nb):
    lpf = 0;
    while nb % 2 == 0:
        lpf = 2;
        nb /= 2;
    for f in range(3, int(sqrt(nb)) + 1, 2):
        while nb % f == 0:
            lpf = f;
            nb /= f;
    if nb > 2: # nb is prime
        lpf = nb;
    return lpf;

print(get_prime_factors(600851475143));
