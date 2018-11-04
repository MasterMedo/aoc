from operator import mul
from itertools import combinations

with open('../input/24.txt') as f:
    data = map(int, f.readlines())

print min(set(reduce(mul, i) for i in combinations(data, 6) if sum(i) == sum(data) / 3))
print min(set(reduce(mul, i) for i in combinations(data, 4) if sum(i) == sum(data) / 4))
