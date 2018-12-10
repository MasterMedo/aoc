from re import findall
from itertools import count

data = [map(int, findall(r'-?\d+', i)) for i in open('../input/10.txt').readlines()]

area = lambda x1, x2, y1, y2: (x2 - x1)*(y2 - y1)
boundaries = lambda xs, ys: [min(xs), max(xs), min(ys), max(ys)]
coord = lambda data, sec: [(x + vx*sec, y + vy*sec) for x, y, vx, vy in data]
size = lambda data, sec: area(*boundaries(*zip(*coord(data, sec))))

sec = next(sec for sec in count() if size(data, sec) < size(data, sec+1))

data = coord(data, sec)
x1, x2, y1, y2 = boundaries(*zip(*data))
for j in range(y1, y2 + 1):
    print ''.join('#' if (i, j) in data else ' ' for i in range(x1, x2 + 1))

print sec
