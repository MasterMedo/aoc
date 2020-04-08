import re
from heapq import heappush, heappop
from functools import lru_cache

@lru_cache(None)
def gindex(xy):
    if   xy == txy:    g = 0
    elif xy.real == 0: g = 48271 * xy.imag
    elif xy.imag == 0: g = 16807 * xy.real
    else:              g = gindex(xy-1) * gindex(xy-1j)
    return int(g+depth) % 20183

with open('../input/22.txt') as f:
    depth, tx, ty = map(int, re.findall('\d+', f.read()))

txy = complex(tx, ty)
erosion = lambda xy: gindex(xy) % 3
print(sum(erosion(x+y*1j) for x in range(tx+1) for y in range(ty+1)))

# heuristic, distance, xy, gear
explore = [(0, 0, 0, 0, 1), (0, 0, 7, 0, 2)]
distance = {(0, 1): 0, (0, 2): 7}
c = 0 # number of visited nodes

while explore[0][-2:] != (txy, 1):
    *_, d, xy, g = heappop(explore)
    if distance[xy, g] < d:
        continue

    for zw in [xy+1, xy-1, xy+1j, xy-1j]:
        if zw.real >= 0 and zw.imag >= 0:
            for tg in range(3):
                if tg != erosion(xy) and tg != erosion(zw):
                    td = d+1 if g == tg else d+8
                    if distance.get((zw, tg), float('inf')) > td:
                        distance[zw, tg] = td
                        heappush(explore, (abs(zw-txy)+td, c:=c+1, td, zw, tg))

print(distance[txy, 1])
