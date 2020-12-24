"""
Abandon hope, all ye who enter here!
Hopefully this will be reworked soon.
"""
import numpy as np
from math import prod, isqrt
from numpy import rot90 as rot, flipud as f
from collections import defaultdict, deque


def get_configurations(arr):
    rarr = rot(arr)
    rrarr = rot(rarr)
    rrrarr = rot(rrarr)
    return [arr, rarr, rrarr, rrrarr, f(arr), f(rarr), f(rrarr), f(rrrarr)]


# data[tile][rotation] -> 2d array of bools
data = {}
with open('../input/20.txt') as fp:
    for chunk in fp.read().split('\n\n'):
        key, *lines = chunk.splitlines()
        arr = np.array([[c == '#' for c in line] for line in lines])
        data[int(key.split()[1][:-1])] = get_configurations(arr)

TILE_SIZE = len(lines)
SIZE = isqrt(len(data))

seen = set()
# matches[tile, rotation][tile, rotation] -> direction
# direction: (tb -> top-bottom, lr -> left-right...)
matches = defaultdict(dict)
for n1 in data:
    for n2 in data:
        if n1 != n2 and (s := frozenset([n1, n2])) not in seen:
            seen.add(s)
            for r1, g1 in enumerate(data[n1]):
                for r2, g2 in enumerate(data[n2]):
                    m = frozenset([(n1, r1), (n2, r2)])
                    if np.array_equal(g1[-1], g2[0]):
                        matches[n1, r1][n2, r2] = 'tb'
                        matches[n2, r2][n1, r1] = 'bt'
                    if np.array_equal(g1[0], g2[-1]):
                        matches[n1, r1][n2, r2] = 'bt'
                        matches[n2, r2][n1, r1] = 'tb'
                    if np.array_equal(g1[:, 0], g2[:, -1]):
                        matches[n1, r1][n2, r2] = 'rl'
                        matches[n2, r2][n1, r1] = 'lr'
                    if np.array_equal(g1[:, -1], g2[:, 0]):
                        matches[n1, r1][n2, r2] = 'lr'
                        matches[n2, r2][n1, r1] = 'rl'

# neighbours[tile][direction] -> number of neighbours
neighbours = defaultdict(lambda: defaultdict(int))
for n1, r1 in matches:
    for n2, r2 in matches[n1, r1]:
        neighbours[n1, r1][matches[n1, r1][n2, r2]] += 1

corners = set()
ns, rs = None, None
for n, r in neighbours:
    if len(neighbours[n, r]) == 2:
        corners.add(n)
        ns, rs = n, r

print(prod(corners))
corner = corners.pop()
rotation = next(i for i in range(8)
                if set(matches[corner, i].values()) == {'lr', 'tb'})

image = [[None]*SIZE for _ in range(SIZE)]
image[0][0] = corner, rotation

# Fit a corner into the top left.
# Visit fitted tiles while all their neighbours are not resolved.
# If only one tile fits into a space put it there and add it to fitted tiles.
seen = {corner}
visit = deque([(0, 0, corner, rotation)])
while len(seen) < SIZE*SIZE:
    r, c, tile, rotation = visit.popleft()
    neighbours = {(a, b): d for (a, b), d in matches[tile, rotation].items()
                  if a not in seen}
    directions = list(neighbours.values())
    for row, col, d in [(r, c-1, 'rl'), (r, c+1, 'lr'),
                        (r-1, c, 'bt'), (r+1, c, 'tb')]:
        if 0 <= row < SIZE and 0 <= col < SIZE and\
                image[row][col] is None and directions.count(d) == 1:
            t = next(t for t, d_ in neighbours.items() if d_ == d)
            image[row][col] = t
            assert t[0] not in seen, (t, row, col)
            seen.add(t[0])
            visit.append((row, col, *t))

    if any(image[row][col] is None for row, col in [(r, c-1), (r, c+1),
                                                    (r-1, c), (r+1, c)]
           if 0 <= row < SIZE and 0 <= col < SIZE):
        visit.append((r, c, tile, rotation))

# merge all the tiles in the image cutting their corners
rows = [[] for _ in range(SIZE*(TILE_SIZE-2))]
for row in range(SIZE):
    for col in range(SIZE):
        tile, r = image[row][col]
        for i in range(1, TILE_SIZE-1):
            rows[row*(TILE_SIZE-2)+i-1].extend(data[tile][r][i][1:-1])

arr = np.array(rows)
monster = """\
                  # \n\
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

for image in get_configurations(arr):
    seamonsters = 0
    for row in range(SIZE*(TILE_SIZE-2) - len(monster)):
        for col in range(SIZE*(TILE_SIZE-2) - len(monster[0])):
            if all(image[row+r][col+c]
                   for r in range(len(monster))
                   for c in range(len(monster[0]))
                   if monster[r][c] == '#'):
                seamonsters += 1
    if seamonsters:
        s = sum(c for row in image for c in row)
        print(s - seamonsters*15)
