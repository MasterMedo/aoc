def code(line):
    x = 13
    for i in line:
        if grid.get(x + move[i]):
            x += move[i]
    return '%x'.upper() % grid[x]

with open('../input/2.txt') as f:
    data = f.read().strip().splitlines()

move = {'R': 1, 'L': -1, 'U': -5, 'D': 5}

grid = {7: 1, 8: 2, 9: 3, 12: 4, 13: 5, 14: 6, 17: 7, 18: 8, 19: 9}
print ''.join(map(code, data))

grid = {3: 1, 7: 2, 8: 3, 9: 4, 11: 5, 12: 6, 13: 7, 14: 8, 15: 9, 17: 10, 18: 11, 19: 12, 23: 13}
print ''.join(map(code, data))
