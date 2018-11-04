from operator import mul
from itertools import combinations as comb

with open("../input/2.txt") as f:
  edges = [map(int, line.split('x')) for line in f.readlines()]

s = 0
for edge in edges:
    areas = map(lambda x: x[0] * x[1], comb(edge, 2))
    s += sum(map((2).__mul__, areas)) + min(areas)
print s

print sum(2 * sum(sorted(edge)[:2]) + reduce(mul, edge) for edge in edges)
