import re
from collections import defaultdict

magic = lambda point: tuple(zip(*zip(*[iter(point)]*3)))
with open('../input/20.txt') as f:
    points = [map(int, re.findall('-?\d+', line)) for line in f]
    points = list(map(magic, points))

t = 1000 # TODO code an algebraic solution

print(min((sum((s + v*t + a*t**2)**2 for s, v, a in point)**1/2, i)
    for i, point in enumerate(points))[1])

for _ in range(t):
    position = defaultdict(list)
    for i, point in enumerate(points):
        points[i] = tuple((s+v+a, v+a, a) for s, v, a in point)
        point = next(zip(*points[i]))
        position[point].append(i)
    remove = [i for l in position.values() for i in l if len(l) > 1]
    for i in sorted(remove, reverse=True):
        del points[i]

print(len(points))
