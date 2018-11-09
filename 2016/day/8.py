import numpy as np
with open('../input/8.txt') as f:
    data = [i.split() for i in f.readlines()]

grid = np.zeros((6, 50))
for i in data:
    if i[0] == 'rect':
        y, x = map(int, i[1].split('x'))
        grid[0: x, 0: y] = np.ones((x, y))
    else:
        x, n = int(i[-3].split('=')[1]), int(i[-1])
        if i[1] != 'row': grid = np.transpose(grid)
        grid[x] = np.roll(grid[x], n)
        if i[1] != 'row': grid = np.transpose(grid)

print int(np.sum(grid))

for k in [''.join(map(lambda x: '.' if x == 0 else '#', j)) for j in grid]:
    print k
