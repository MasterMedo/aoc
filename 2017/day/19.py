with open('../input/19.txt') as f:
    grid = {x+y*1j: c for y, l in enumerate(f) for x, c in enumerate(l)}

xy = next(xy for xy in grid if xy.imag == 0 and grid[xy] != ' ')
block = {1: '-', -1: '-', 1j: '|', -1j: '|'}
letters = ''
steps = 0
d = 1j
while grid[xy] != ' ':
    if grid[xy] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        letters += grid[xy]

    if grid[xy] == '+':
        d *= 1j if grid[xy+d*1j] == block[d*1j] else 1j**-1

    xy += d
    steps += 1

print(letters)
print(steps)
