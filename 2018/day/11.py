from collections import defaultdict
number = int(open('../input/11.txt').read())

grid = defaultdict(int)
for y in xrange(301):
    for x in xrange(301):
        elem = (((((x + 10) * y) + number) * (x + 10))//100%10)-5
        grid[x, y] = grid[x-1, y] + elem + grid[x, y-1] - grid[x-1, y-1]

d = {}
rect = lambda x, y, n: grid[x, y] - grid[x-n, y] - grid[x, y-n] + grid[x-n, y-n]
print d[max(rect(x, y, 3) for x in range(301) for y in range(301) if not d.update({rect(x, y, 3): (x-2, y-2)}))]
print d[max(rect(x, y, n) for x in range(301) for y in range(301) for n in range(20) if not d.update({rect(x, y, n): (x-n+1, y-n+1, n)}))]
