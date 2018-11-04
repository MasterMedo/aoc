def walk(n, i, x):
    for _ in xrange(n):
        xy[i] += x
        if tuple(xy) in grid and not part2:
            part2.append(abs(xy[0]) + abs(xy[1]))
        grid.append(tuple(xy))

with open('../input/1.txt') as fp:
    data = fp.read().strip().split(', ')

part2, grid, xy, angle = [], [], [0, 0], 0
sides = ((1, 1), (0, 1), (1, -1), (0, -1))
for i in data:
    angle += 1 if i[0] == 'R' else -1
    angle %= 4
    walk(int(i[1:]), *sides[angle])

print abs(xy[0]) + abs(xy[1])
print part2.pop()
