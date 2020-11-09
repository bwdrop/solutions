#!/usr/bin/python3

MAX = 1000000
chain_map = {}

def collatz_sequence(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1

def get_chain_count(n):
    if n == 1:
        chain_map[n] = 1
        return 1
    elif n in chain_map != None:
        return chain_map[n]
    else:
        res = 1 + get_chain_count(collatz_sequence(n))
        chain_map[n] = res
        return res

max_chain_nb = 1
max_chain_count = 0
for i in range(1, MAX):
    res = get_chain_count(i)
    if res > max_chain_count:
        max_chain_count = res
        max_chain_nb = i

print(max_chain_nb, max_chain_count)