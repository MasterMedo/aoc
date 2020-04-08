from collections import defaultdict
intcode = __import__('9').intcode
from blessed import Terminal
term = Terminal()

with open('../input/13.txt') as f:
    tape = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

def player_input():
    key = {'h': -1, 'LEFT': -1, 'l': 1, 'RIGHT': 1}
    while True:
        # print(term.home, end='', flush=True)
        # for y in range(50, 0, -1):
        #     print(''.join(' |#_*'[grid.get((x, y), 0)] for x in range(50)))
        # char = term.inkey()
        # yield key.get(char.name[4:] if char.is_sequence else char, 0)
        yield -1 if ball < player else ball > player

def handle_output():
    global x, y, player, ball, score
    while True:
        x = yield
        y = yield
        t = yield
        if   t <= 4: grid[x, y] = t
        if   t == 3: player = x
        elif t == 4: ball = x
        elif t >  4: score = t

score, grid = 0, {}
tape[0] = 2 # comment for part one
(output := handle_output()).send(None)
with term.cbreak(), term.hidden_cursor():
    for instruction in intcode(tape, player_input()):
        output.send(instruction)

print(f'blocks: {sum(grid[k] == 2 for k in grid)}')
print(f'score: {score}')
