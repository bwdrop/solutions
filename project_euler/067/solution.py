#!/usr/bin/python3

# Same code as problem #18

# Parsing
def load_file(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            for ch in line.strip('\n').split(' '):
                numbers.append(int(ch))
    return numbers

# Init
triangle = load_file('triangle.txt')
max_size = len(triangle)
max_sum_tree = [0] * max_size

# Tree navigation
def childs(i, lvl):
    return (i + lvl, i + lvl + 1) if i + lvl < max_size else (-1, -1)

def run_through_tree(i, lvl):
    (left, right) = childs(i, lvl)
    if (left, right) == (-1, -1):
        max_sum_tree[i] = triangle[i]
        return triangle[i]
    if max_sum_tree[left] == 0:
        run_through_tree(left, lvl + 1)
    if max_sum_tree[right] == 0:
        run_through_tree(right, lvl + 1)
    if max_sum_tree[left] > 0 and max_sum_tree[right] > 0:
        max_sum_tree[i] = triangle[i] + max(max_sum_tree[left], max_sum_tree[right])
        return max_sum_tree[i]

run_through_tree(0, 1)
print(max_sum_tree[0])
