#!/usr/bin/python3

from functools import reduce

def sum_of_squares(numbers):
    return reduce((lambda x, y: x + y), map(lambda x: x**2, numbers));

def square_of_sum(numbers):
    return reduce((lambda x, y: x + y), numbers)**2;

print(abs(sum_of_squares(range(101)) - square_of_sum(range(101))));
