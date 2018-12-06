def closest(x, y):
    m = min(distance(x, y))
    return next(n for n, (i, j) in enumerate(data) if abs(x-i) + abs(y-j) == m) 

data = [map(int, i.split(', ')) for i in open('../input/6.txt').readlines()]

side = max(max(zip(*data)[0]), max(zip(*data)[1]))
distance = lambda x, y: [abs(x-i) + abs(y-j) for i, j in data]
eqidistant = set((x, y) for x in xrange(side) for y in xrange(side) if distance(x, y).count(min(distance(x, y))) > 1)
grid = {(x, y): closest(x, y) if (x, y) not in eqidistant else -1 for x in xrange(side) for y in xrange(side)}
inf = set(grid[x, y] for edge in xrange(side) for x, y in [(edge, side-1), (edge, 0), (side-1, edge), (0, edge)])

print max(grid.values().count(n) for n in range(len(data)) if n not in inf)
print sum(sum(distance(x, y)) < 10000 for x in xrange(side) for y in xrange(side))
