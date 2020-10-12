from collections import defaultdict
from heapq import heappop, heappush


grid = defaultdict(lambda: '#')
portals = defaultdict(list)
with open('../input/20.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line[:-1]):
            if c.isupper():
                if (c2 := grid[x-1, y]).isupper():
                    portals[c2 + c].append((x-2, y) if grid[x-2, y] == '.' else
                                           (x+1, y))

                elif (c2 := grid[x, y-1]).isupper():
                    portals[c2 + c].append((x, y-2) if grid[x, y-2] == '.' else
                                           (x, y+1))

            grid[x, y] = c

teleport = {}
for portal, xys in portals.items():
    if portal == 'AA':
        start = (0, *xys[0])
    elif portal == 'ZZ':
        end = xys[0]
    else:
        xy, zw = xys
        teleport[xy] = zw, [-1, 1][5 < xy[0] < x-5 and 5 < xy[1] < y-5]
        teleport[zw] = xy, [-1, 1][5 < zw[0] < x-5 and 5 < zw[1] < y-5]

first = True
to_visit = []
visited = set()
heappush(to_visit, (0, *start, 0))
while to_visit:
    distance, z, x, y, die = heappop(to_visit)

    if (x, y) == end:
        if first:
            first = False
            print(distance)

        if z == 0:
            print(distance)
            break

    for xy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if (z, *xy) not in visited and grid[xy] == '.':
            visited.add((z, *xy))
            inc, z_ = 1, 0
            if xy in teleport:
                xy, z_ = teleport[xy]
                visited.add((z+z_, *xy))
                inc += 1

            part1 = False
            if z + z_ < 0:
                part1 = True

            if first or 0 <= z + z_ < 30 and not die:  # increase 30 if need be
                heappush(to_visit, (distance + inc, z + z_, *xy, die or part1))
