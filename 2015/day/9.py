from itertools import permutations, chain

with open('../input/9.txt') as f:
    edges = {frozenset({x, y}): int(z) for x, _, y, _, z in map(str.split, f)}

cities = set(chain(*edges))
paths = [sum(edges[frozenset({x, y})] for x, y in zip(p[:-1], p[1:]))
         for p in permutations(cities)]

print(min(paths))
print(max(paths))
