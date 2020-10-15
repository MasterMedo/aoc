from heapq import heappop, heappush
from collections import defaultdict


def set_dist_and_doors(grid):
    global dist, doors
    dist, doors = {}, {}
    for key in keys:
        x, y = keys[key]
        to_visit = [(0, x, y, frozenset())]
        visited = set()
        dist[key] = defaultdict(lambda: float('inf'))
        doors[key] = defaultdict(set)
        while to_visit:
            distance, x, y, gates = heappop(to_visit)

            for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                key_ = grid.get((x_, y_), '#')
                gates_ = gates | {key_.lower()} if key_.isupper() else gates
                if (x_, y_) not in visited and key_ != '#':
                    if key_ in keys:
                        dist[key][key_] = distance + 1
                        doors[key][key_] = gates_
                        continue

                    visited.add((x_, y_))
                    heappush(to_visit, (distance + 1, x_, y_, gates_))


keys, grid = dict(), dict()
with open('../input/18.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line[:-1]):
            grid[x, y] = c
            if c.islower() or c == '@':
                keys[c] = x, y

set_dist_and_doors(grid)
to_visit = [(0, '@', frozenset('@'))]
visited = set()
while to_visit:
    distance, key, on_me = heappop(to_visit)

    if len(on_me) >= len(keys):
        break

    for key_ in dist[key].keys():
        on_me_ = on_me | {key_}
        if doors[key][key_] <= on_me and (key_, on_me_) not in visited:
            visited.add((key_, on_me_))
            heappush(to_visit, (distance + dist[key][key_], key_, on_me_))

print(distance)

x, y = keys.pop('@')
for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
    grid[x_, y_] = '#'

for i, (x_, y_) in enumerate([(x+1, y+1), (x-1, y+1), (x+1, y-1), (x-1, y-1)]):
    grid[x_, y_] = str(i)
    keys[str(i)] = x_, y_

set_dist_and_doors(grid)
to_visit = [(0, '0123', frozenset('0123'))]
visited = set()
while to_visit:
    distance, bots, on_me = heappop(to_visit)

    if len(on_me) >= len(keys):
        break

    for i, key in enumerate(bots):
        for key_ in dist[key].keys():
            bots_ = bots[:i] + key_ + bots[i+1:]
            on_me_ = on_me | {key_}
            if doors[key][key_] <= on_me and (bots_, on_me_) not in visited:
                visited.add((bots_, on_me_))
                heappush(to_visit, (distance + dist[key][key_], bots_, on_me_))

print(distance)
