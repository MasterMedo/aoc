from collections import defaultdict

def comb2(x):
    comb = [x]
    for _ in range(4):
        i, j, _, k, l = comb[-1]
        comb.append(j+i+'/'+l+k) # flip
        comb.append(k+i+'/'+l+j) # rotate
    return comb[1:]

def comb3(x):
    comb = [x]
    for _ in range(4):
        a, b, c, _, d, e, f, _, g, h, i = comb[-1]
        comb.append(g+h+i+'/'+d+e+f+'/'+a+b+c) # flip
        comb.append(c+b+a+'/'+f+e+d+'/'+i+h+g) # flip
        comb.append(g+d+a+'/'+h+e+b+'/'+i+f+c) # rotate
    return comb[1:]

data = {}
with open('../input/21.txt') as f:
    for line in f:
        x, y = line[:-1].split(' => ')
        comb = comb2(x) if len(x) == 5 else comb3(x)
        for x in comb:
            data[x] = y

grid = {0: '.#.', 1: '..#', 2: '###'}
for i in range(1, 19):
    size = len(grid[0])
    mod = 3 if size%2 else 2
    next_grid = defaultdict(str)

    for y in range(0, size, mod):
        for x in range(0, size, mod):
            block = '/'.join(grid[y+dy][x:x+mod] for dy in range(mod))
            for dy, line in enumerate(data[block].split('/')):
                next_grid[y//mod*(mod+1)+dy] += line

    grid = next_grid
    if i == 5 or i == 18:
        print(sum(c == '#' for c in ''.join(grid.values())))
