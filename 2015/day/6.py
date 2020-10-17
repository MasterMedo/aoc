import numpy as np

with open('../input/6.txt') as f:
    data = [line.replace(',', ' ').split() for line in f.readlines()]

grid = np.zeros((1000, 1000))
for *cmd, x, y, _, z, w in data:
    x, y, z, w = map(int, [x, y, z, w])
    if cmd[0] == 'toggle':
        grid[x:z+1, y:w+1] = 1 - grid[x:z+1, y:w+1]
        # grid[x:z+1, y:w+1] += 2

    elif cmd[1] == 'on':
        grid[x:z+1, y:w+1] = 1  # = -> +=

    elif cmd[1] == 'off':
        grid[x:z+1, y:w+1] = -1  # = -> +=

    grid[grid < 0] = 0

print(int(np.sum(grid)))
