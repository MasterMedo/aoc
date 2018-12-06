from collections import Counter

data = [map(int, i.split(', ')) for i in open('../input/6.txt').readlines()]

max_x = max(zip(*data)[0])
max_y = max(zip(*data)[1])
grid={}
for i in range(max_x):
    for j in range(max_y):
        m = min(abs(i-k)+abs(j-l) for k, l in data)
        for n, (k, l) in enumerate(data):
            if abs(i-k)+abs(j-l) == m:
                if grid.get((i, j), -1) != -1:
                    grid[i, j] = -1
                    break
                grid[i, j] = n

s = set([-1])
s = s.union(set(grid[x, max_y-1] for x in range(max_x)))
s = s.union(set(grid[x,       0] for x in range(max_x)))
s = s.union(set(grid[max_x-1, y] for y in range(max_y)))
s = s.union(set(grid[      0, y] for y in range(max_y)))

print next(i[1] for i in Counter(grid.values()).most_common() if i[0] not in s)
print sum(sum(abs(i-k)+abs(j-l) for k, l in data) < 10000 for i in range(max_x) 
                                                          for j in range(max_y))
