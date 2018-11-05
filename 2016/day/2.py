def code(line):
    x = 5
    for i in line:
        if   i == 'R' and x % 3 != 0: x += 1
        elif i == 'L' and x % 3 != 1: x -= 1
        elif i == 'U' and 9 >= x > 3: x -= 3
        elif i == 'D' and 1 <= x < 7: x += 3
    return str(x)

with open('../input/2.txt') as f:
    data = f.read().strip().splitlines()

print ''.join(map(code, data))

grid = {(0, 2): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (-2, 0): 5, (-1, 0): 6, (0, 0): 7, (1, 0): 9, (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C', (0, -2): 'D'}
x, y = -2, 0
for i in data:
    for j in i:
	if j == 'R': x = min(x + 1,  (2 - abs(y)))
	if j == 'L': x = max(x - 1, -(2 - abs(y)))
	if j == 'U': y = min(y + 1,  (2 - abs(x)))
	if j == 'D': y = max(y - 1, -(2 - abs(x)))
    print grid[x, y],
