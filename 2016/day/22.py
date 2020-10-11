import re
from heapq import heappop, heappush


with open('../input/22.txt') as f:
    data = [list(map(int, re.findall(r'[0-9]+', line))) for line in f]

xy, full = next((xy, size) for *xy, size, _, _, use in data[2:] if use == 0)
nodes = {(x, y): (use <= full) + (use == 0) for x, y, _, use, *_ in data[2:]}
print(sum(nodes.values()) - 2)

max_x = max(x for x, *_ in data[2:])
to_visit = []
heappush(to_visit, (0, *xy))
visited = {(*xy)}
while to_visit:
    distance, x, y = heappop(to_visit)
    if y == 0 and x == max_x:
        break

    for xy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if xy in nodes and xy not in visited and nodes[xy]:
            heappush(to_visit, (distance+1, *xy))
            visited.add(xy)

print(distance + 5*(max_x-1))
