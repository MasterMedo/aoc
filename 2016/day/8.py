import numpy as np


with open('../input/8.txt') as f:
    lines = [line.split() for line in f]

grid = np.zeros((6, 50))
for words in lines:
    if words[0] == 'rect':
        y, x = map(int, words[1].split('x'))
        grid[0: x, 0: y] = np.ones((x, y))

    else:
        x, n = int(words[-3].split('=')[1]), int(words[-1])
        if words[1] != 'row':
            grid = np.transpose(grid)

        grid[x] = np.roll(grid[x], n)

        if words[1] != 'row':
            grid = np.transpose(grid)

print(int(np.sum(grid)))

for line in grid:
    print(''.join(' ' if c == 0 else '#' for c in line))
