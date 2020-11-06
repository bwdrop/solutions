#!/usr/bin/python3

for a in range(1, 1001):
    for b in range(a, 1001):
        for c in range(b, 1001):
            if a + b + c == 1000 and c**2 == a**2 + b**2:
                print(a * b * c)
