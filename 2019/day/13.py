from collections import defaultdict
from time import sleep

from blessed import Terminal

intcode = __import__('9').intcode
term = Terminal()

with open('../input/13.txt') as f:
    tape = list(map(int, f.read().split(',')))

def player_input():
    key = {'h': -1, 'LEFT': -1, 'l': 1, 'RIGHT': 1}
    while True:
        # sleep(0.1)
        # print(term.home, end='', flush=True)
        # for y in range(50, 0, -1):
        #     print(''.join(' |#_*'[grid.get((x, y), 0)] for x in range(50)))
        # char = term.inkey()
        # yield key.get(char.name[4:] if char.is_sequence else char, 0)
        yield -1 if ball < player else ball > player

grid = {}
tape[0] = 2 # comment for part one
game = intcode(tape, player_input())
with term.cbreak(), term.hidden_cursor():
    for x in game:
        y = next(game)
        t = next(game)
        if   t <= 4: grid[x, y] = t
        if   t == 3: player = x
        elif t == 4: ball = x

print(f'blocks: {sum(grid[i] == 2 for i in grid)}')
print(f'score: {t}')
