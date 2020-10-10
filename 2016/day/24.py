from heapq import heappush, heappop


grid, keys = {}, {}
with open('../input/24.txt') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line[:-1]):
            grid[x, y] = c
            if c not in '#.':
                keys[c] = (x, y)

first = True
to_visit = []
heappush(to_visit, (0, len(keys)-1, *keys['0'], frozenset('0')))
visited = set([(*keys['0'], frozenset('0'))])
while to_visit:
    distance, keys_left, x, y, keys_ = heappop(to_visit)
    if keys_left <= 0:
        if first:
            first = False
            print(distance)

        if (x, y) == keys['0']:
            break

    for z, w in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        c = grid[z, w]
        if c != '#' and (z, w, keys_) not in visited:
            if c in keys and c not in keys_:
                heappush(to_visit, (distance+1, keys_left-1, z, w, keys_ | {c}))
                visited.add((z, w, keys_ | {c}))
            else:
                heappush(to_visit, (distance+1, keys_left, z, w, keys_))
                visited.add((z, w, keys_))

print(distance)
