from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/11.txt') as f:
    tape = list(map(int, f.read().split(',')))

xy, d = 0j, -1j
colors = defaultdict(int)
colors[0] = 1 # comment for part 1

robot = intcode(tape, (colors[xy] for _ in iter(int, 1)))
for color in robot:
    turn = next(robot)
    colors[xy] = color
    d /= 1j**(-1)**turn
    xy += d

# print(len(colors)) # uncomment for part 1
for y in range(6):
    print(''.join('#' if colors[x+y*1j] else ' ' for x in range(40)))
