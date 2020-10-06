from functools import lru_cache
from heapq import heappop, heappush


@lru_cache
def grid(x, y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + seed).count('1') % 2


goal = 31 + 39j
with open('../input/13.txt') as f:
    seed = int(f.read())

visitable_in_under_50_steps = 0
to_visit = []
heappush(to_visit, (0, 1, 1))  # distance, x, y
visited = set([(1, 1)])
while to_visit:
    distance, x, y = heappop(to_visit)
    if x == goal.real and y == goal.imag:
        break

    if distance <= 50:
        visitable_in_under_50_steps += 1

    xy = x + y * 1j
    for d in [1, -1, 1j, -1j]:
        zw = xy + d
        z, w = int(zw.real), int(zw.imag)
        if z >= 0 and w >= 0 and (z, w) not in visited and not grid(z, w):
            heappush(to_visit, (distance + 1, z, w))
            visited.add((z, w))

print(distance)
print(visitable_in_under_50_steps)
