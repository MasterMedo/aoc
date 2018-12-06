from collections import Counter

data = [map(int, i.split(', ')) for i in open('../input/6.txt').readlines()]

side = max(max(zip(*data)[0]), max(zip(*data)[1]))
man = lambda x, y: (abs(x-i) + abs(y-j) for i, j in data)

grid = {}
for x in xrange(side):
    for y in xrange(side):
        m = min(man(x, y))
        for n, (i, j) in enumerate(data):
            if abs(x-i) + abs(y-j) != m: continue
            grid[x, y] = n if grid.get((x, y), -1) == -1 else -1

inf = set(grid[x, y] for edge in xrange(side) for x, y in [(edge, side-1), (edge, 0), (side-1, edge), (0, edge)])
print next(n[1] for n in Counter(grid.values()).most_common() if n[0] not in inf)
print sum(sum(man(x, y)) < 10000 for x in xrange(side) for y in xrange(side))
