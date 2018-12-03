import re
from collections import Counter

data = [map(int, re.findall(r'\d+', s)) for s in open('../input/3.txt').readlines()]
squares = lambda i: ((j, k) for j in range(i[1], i[1] + i[-2])
                            for k in range(i[2], i[2] + i[-1]))
grid = Counter(x for i in data for x in squares(i))

print sum(n > 1 for n in grid.values())
print next(i[0] for i in data if all(grid[x] == 1 for x in squares(i)))
