from collections import defaultdict, deque
from blessed import Terminal
from time import sleep
intcode = __import__('9').intcode
term = Terminal()

def draw(xy=None):
    with term.hidden_cursor():
        blocks = {-2: ' ', -1: '*', 0: '#', 1: '.', 2: 'O'}
        print(term.home)
        for y in range(21, -20, -1):
            for x in range(-20, 22):
                zw = x + y*1j
                print('D' if zw == xy else blocks[grid[zw]], end='')
            print()
    sleep(0.01)

with open('../input/15.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

xy = 0j
actions = [3, 1, 4, 2]
moves = deque(reversed(actions))
move, power = moves[-1], actions.index(moves[-1])
grid = defaultdict(lambda: -2, {0: -1, 1j: -1, -1j: -1, 1: -1, -1: -1})

for block in intcode(l, (moves.pop() for _ in iter(int, 1))):
    if block == 0: # wall
        grid[xy + 1j**power] = 0

    else:
        xy += 1j**power
        if grid[xy] == -1: # unexplored
            grid[xy] = block
            moves.append(actions[(power+2)%4])
            for p, m in enumerate(actions):
                if grid[xy+1j**p] == -2: # not seen
                    moves.append(m)
                    grid[xy+1j**p] = -1
    # draw(xy)
    if not moves:
        break
    power = actions.index(moves[-1])

visited = set(xy for xy in grid if grid[xy] == 0)
to_visit = deque([(xy, 0) for xy in grid if grid[xy] == 2])
# to_visit = deque([(0, 0)]) # uncomment for part1
depth, block = 0, 2 if grid[to_visit[0][0]] == 2 else -1
while to_visit:
    xy, d = to_visit.popleft()
    if grid[xy] == 2 and d != 0:
        break

    visited.add(xy)
    grid[xy] = block
    for i in range(4):
        if xy + 1j**i not in visited:
            to_visit.append((xy+1j**i, d+1))

    if d > depth:
        # draw()
        depth = d

print(depth)
