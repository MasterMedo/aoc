def walk(n, i, x):
    for _ in range(n):
        xy[i] += x
        if tuple(xy) in grid and not part2:
            part2.append(sum(abs(i) for i in xy))
        grid.append(tuple(xy))

with open('../input/01.txt') as fp:
    data = [i for i in fp.read().strip().split(', ')]

part2, grid, xy, angle = [], [], [0, 0], 0
sides = ((1, 1), (0, 1), (1, -1), (0, -1))
for i in data:
    angle += 1 if i[0] == 'R' else -1
    angle %= 4
    walk(int(i[1:]), *sides[angle])

print sum(abs(i) for i in xy)
print part2.pop()
