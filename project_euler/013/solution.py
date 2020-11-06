#!/usr/bin/python3

from functools import reduce

def load_file(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            num = []
            for ch in line.strip('\n'):
                num.append(int(ch))
            numbers.append(num)
    return numbers

num_list = load_file('sum.txt')

max_num_index = len(num_list[0]) - 1
large_sum = []
for j in range(max_num_index, -1, -1):
    sum = 0
    for i in range(0, len(num_list)):
        sum += num_list[i][j]
    if len(large_sum) > 0 and large_sum[0] // 10 > 0:
        sum += large_sum[0] // 10
        large_sum[0] %= 10
    large_sum.insert(0, sum)

res = reduce((lambda x, y: x + y), map(lambda x: str(x), large_sum))
print(res[:10])
