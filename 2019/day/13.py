from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/13.txt') as f:
    tape = list(map(int, f.read().split(',')))

grid = {}
tape[0] = 2 # comment for part one
player_input = (-1 if ball < player else ball > player for _ in iter(int, 1))
game = intcode(tape, player_input)

for x, y, t in iter(lambda: [next(game) for _ in range(3)], 1):
    if x == -1 and y == 0 and t == 0:
        print(sum(grid[i] == 2 for i in grid))

    if   t <= 4: grid[x, y] = t
    if   t == 3: player = x
    elif t == 4: ball = x

print(t)
