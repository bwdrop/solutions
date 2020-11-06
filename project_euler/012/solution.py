#!/usr/bin/python3

import math

def factors(n):
    factors = []
    for i in range(1, math.isqrt(n)):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n // i)
    return factors

nbFactors = []
index = 0
triangle = 0
while len(nbFactors) < 500:
    index += 1
    triangle += index
    nbFactors = factors(triangle)

print(index, triangle, len(nbFactors))

