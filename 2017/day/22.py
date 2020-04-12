from collections import defaultdict

with open('../input/22.txt') as f:
    grid = defaultdict(int, {x+y*1j: (c=='#')*2 for y, l in enumerate(f)
                                                for x, c in enumerate(l[:-1])})
d = -1j
counter = 0
xy = (1+1j) * ((len(grid)**(1/2))//2)
for burst in range(10000000):
    d *= 1j**(4-(grid[xy]^1))
    grid[xy] = (grid[xy]+1)%4
    if grid[xy] == 2:
        counter += 1
    xy += d

print(counter)
