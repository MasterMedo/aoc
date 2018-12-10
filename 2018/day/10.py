from re import findall
from itertools import count

data = [map(int, findall(r'-?\d+', i)) for i in open('../input/10.txt').readlines()]

area       = lambda x1, x2, y1, y2: (x2 - x1)*(y2 - y1)
coords     = lambda data, sec:      [(x + vx*sec, y + vy*sec) for x, y, vx, vy in data]
boundaries = lambda xs, ys:         [min(xs), max(xs), min(ys), max(ys)]
box_size   = lambda data, sec:      area(*boundaries(*zip(*coords(data, sec))))

sec = next(sec for sec in count() if box_size(data, sec) < box_size(data, sec + 1))

points = coords(data, sec)
x1, x2, y1, y2 = boundaries(*zip(*points))
for j in range(y1, y2 + 1):
    print ''.join('#' if (i, j) in points else ' ' for i in range(x1, x2 + 1))

print sec
