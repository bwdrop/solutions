#!/usr/bin/python3

from functools import reduce

def load_file(filename):
    num = [];
    with open(filename) as f:
        for line in f:
            for ch in line.strip('\n'):
                num.append(int(ch));
    return num;

num_list = load_file('num.txt');

length = 13;
maxp = 0;

for i in range(0, len(num_list) - length + 1):
    p = reduce((lambda x, y: x * y), num_list[i:i + length]);
    if p > maxp:
        maxp = p;

print(maxp);
