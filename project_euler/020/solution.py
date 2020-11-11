#!/usr/bin/python3
"""
# Title
Factorial digit sum

# URL
https://projecteuler.net/problem=20

# Problem
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

# Solved by
Heliane Ly
November 2020

# Algorithm
"""
factorial = 1
for n in range(2, 101):
    factorial *= n
print(sum([int(ch) for ch in str(factorial)]))
