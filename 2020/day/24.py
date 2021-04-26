from collections import defaultdict
import re

d = {
    'e': 1,
    'se': 0.5+1j,
    'ne': 0.5-1j,
    'w': -1,
    'sw': -0.5+1j,
    'nw': -0.5-1j,
}

grid = defaultdict(bool)
with open('../input/24.txt') as f:
    for line in f:
        grid[sum(d[cmd] for cmd in re.findall('e|se|ne|w|sw|nw', line))] ^= 1

print(sum(grid.values()))

for i in range(100):
    for tile in grid.keys():
        for n in d.values():
            grid[tile+n]

    grid_ = grid.copy()
    for tile in grid_.keys():
        bt = sum(grid[tile+n] for n in d.values())
        if grid[tile] and (bt == 0 or bt > 2):
            grid_[tile] ^= 1
        elif not grid[tile] and bt == 2:
            grid_[tile] ^= 1
    grid = grid_

print(sum(grid.values()))
