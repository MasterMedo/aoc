from operator import mul
from itertools import combinations as comb

with open("../input/2.txt") as f:
  rows = [map(int, line.split('x')) for line in f.readlines()]

print sum(2 * side for row in rows for side in map(lambda x: x[0] * x[1], comb(row, 2))) \
        + sum(min(map(lambda x: x[0] * x[1], comb(row, 2))) for row in rows)
print sum(2 * sum(sorted(row)[:2]) + reduce(mul, row) for row in rows)
