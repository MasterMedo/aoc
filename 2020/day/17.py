from itertools import product
from collections import defaultdict


def count_active(active, dimension, cycles=6):
    active = set((0,) * (dimension-2) + cube for cube in active)
    for _ in range(cycles):
        new_active = set()
        neighbours = defaultdict(int)
        for cube in active:
            for offset in product((-1, 0, 1), repeat=dimension):
                if offset != (0,) * dimension:
                    neighbour = tuple(x + dx for x, dx in zip(cube, offset))
                    neighbours[neighbour] += 1

        for cube, n in neighbours.items():
            if cube in active and n in [2, 3]:
                new_active.add(cube)

            elif cube not in active and n == 3:
                new_active.add(cube)

        active = new_active
    return len(active)


with open('../input/17.txt') as f:
    active = set((r, c) for r, line in enumerate(f.read().splitlines())
                 for c, n in enumerate(line) if n == '#')

print(count_active(active, 3))
print(count_active(active, 4))
