from re import findall
from itertools import count

data = [map(int, findall(r'-?\d+', i)) for i in open('../input/10.txt').readlines()]

area = lambda x1, x2, y1, y2: (x2 - x1)*(y2 - y1)
coord = lambda (x, y, vx, vy): (x + vx*sec, y + vy*sec)
boundaries = lambda xs, ys: [min(xs), max(xs), min(ys), max(ys)]

min_box = float('inf')
for sec in count():
    box = area(*boundaries(*zip(*map(coord, data))))
    if box > min_box:
        break
    min_box = box

sec -= 1
data = map(coord, data)
x1, x2, y1, y2 = boundaries(*zip(*data))
for j in range(y1, y2 + 1):
    print ''.join('#' if (i, j) in data else ' ' for i in range(x1, x2 + 1))

print(sec)
