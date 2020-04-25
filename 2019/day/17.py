from collections import defaultdict
from itertools import takewhile, count, chain
intcode = __import__('9').intcode

with open('../input/17.txt') as f:
    tape = list(map(int, f.read().split(',')))

direction = {'^': -1j, 'v': 1j, '>': 1, '<': -1}
grid = defaultdict(lambda: '.')
zw = xy = 0j
d = None
for c in map(chr, intcode(tape, None)):
    if c == '\n':
        zw = (zw.imag+1)*1j
        continue
    elif c in direction:
        d = direction[c]
        xy = zw
    grid[zw] = c
    zw += 1

alignment = 0
for zw in dict(grid):
    if grid[zw] == '#' and all(grid[zw+d] == '#' for d in direction.values()):
        alignment += zw.real * zw.imag

print(int(alignment))

path = []
forward = 0
while '#' in {grid[xy+d], grid[xy+d*1j], grid[xy+d/1j]}:
    if grid[xy+d] == '#':
        forward += 1
        xy += d
        continue

    if forward:
        path.append(forward)
        forward = 0

    if   grid[xy+d*1j] == '#':
        path.append('R')
        d *= 1j

    elif grid[xy+d/1j] == '#':
        path.append('L')
        d /= 1j

path.append(forward)

# print(path) # manually get: A, B, C ain't that hard
path = list(map(str, path))

def robot_input(*patterns):
    for pattern in patterns:
        for c in pattern:
            yield ord(c)
    yield ord('n')
    yield ord('\n')

main = 'A,C,A,C,B,B,C,A,C,B\n'
A = 'L,8,R,12,R,12,R,10\n'
B = 'L,10,R,10,L,6\n'
C = 'R,10,R,12,R,10\n'

tape[0] = 2
for output in intcode(tape, robot_input(main, A, B, C)):
    if output > 50000:
        print(output)
