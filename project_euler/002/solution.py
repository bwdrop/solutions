#!/usr/bin/python3

from functools import reduce

fib_list = [1, 2]

def generate_fib_list():
    fib = 0
    while fib <= 4000000:
        i = len(fib_list)
        fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(fib)

generate_fib_list()

print(reduce((lambda x, y: x + y), filter(lambda x: x % 2 == 0, fib_list)))
