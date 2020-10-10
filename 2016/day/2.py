def walk(instructions):
    x = 13
    for i in instructions:
        x_ = x + move[i]
        if -1 < x_ < len(grid) and grid[x_] != '_':
            x = x_

    return grid[x]


move = {'R': 1, 'L': -1, 'U': -5, 'D': 5}

with open('../input/2.txt') as f:
    lines = f.read().strip().splitlines()

grid = '_____' '_123_' '_456_' '_789_' '_____'
print(''.join(map(walk, lines)))

grid = '__1__' '_234_' '56789' '_ABC_' '__D__'
print(''.join(map(walk, lines)))
