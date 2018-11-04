f = {
        "^": lambda xy: (xy[0] - 1, xy[1]),
        "v": lambda xy: (xy[0] + 1, xy[1]),
        "<": lambda xy: (xy[0], xy[1] - 1),
        ">": lambda xy: (xy[0], xy[1] + 1)
    }

with open('../input/3.txt') as fp:
    data = fp.read().strip()

grid, xy = {(0, 0): 1}, [[0, 0], [0, 0]]
for i in xrange(len(data)):
    # mod = 0
    mod = i % 2
    xy[mod] = f[data[i]](xy[mod])
    if xy[mod] not in grid:
        grid[xy[mod]] = 0
    grid[xy[mod]] += 1

print len(grid)
