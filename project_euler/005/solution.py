#!/usr/bin/python3

from functools import reduce

def greatest_common_divisor(a, b):
    if b == 0:
        return a;
    return greatest_common_divisor(b, a % b);

def least_common_multiple(a, b):
    return (a / greatest_common_divisor(a, b)) * b;

print(reduce((lambda a, b: least_common_multiple(a, b)), range(1, 21)));
