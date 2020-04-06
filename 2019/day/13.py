from collections import defaultdict
from blessed import Terminal
intcode = __import__('9').intcode

with open('../input/13.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

term = Terminal()
block = {0: ' ', 1: '|', 2: '#', 3: '_', 4: '*'}
key = defaultdict(int, {'h': -1, 'LEFT': -1, 'l': 1, 'RIGHT': 1})

def player_input():
    while True:
        print(term.home, end='', flush=True)
        for y in range(50, 0, -1):
            print(''.join(block[grid[x, y]] for x in range(50)), flush=True)

        char = term.inkey()
        yield key[char] if not char.is_sequence else key[char.name[4:]]

score = x = y = 0
grid = defaultdict(int)
l[0] = 2 # comment for part one
with term.cbreak(), term.hidden_cursor():
    for i, o in enumerate(intcode(l, player_input())):
        if i % 3 == 0:
            x = o
        elif i % 3 == 1:
            y = o
        elif o > 4:
            score = o
        else:
            grid[x, y] = o

print(f'blocks: {sum(grid[k] == 2 for k in grid)}')
print(f'score: {score}')
