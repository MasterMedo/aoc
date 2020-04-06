from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/11.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

xy, d = 0j, 1j
grid = defaultdict(int)
grid[0] = 1 # comment for part 1

for i, o in enumerate(intcode(l, (grid[xy] for _ in iter(int, 1)))):
    if i % 2 == 0:
        grid[xy] = o
    else:
        d *= 1j**(-1)**o
        xy += d

# print(len(grid)) # uncomment for part 1
for y in range(0, -6, -1):
    for x in range(0, 40):
        print('#' if grid[x+y*1j] else ' ', end='')
    print()
