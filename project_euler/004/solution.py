#!/usr/bin/python3

def is_palyndrome(x):
    return str(x) == str(x)[::-1];

lp = 0;

for a in range(900, 1000):
    for b in range(900, 1000):
        p = a * b;
        if is_palyndrome(p) and p > lp:
            lp = p;

print(lp);
