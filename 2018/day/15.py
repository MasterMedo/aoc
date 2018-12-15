from copy import deepcopy
from math import ceil

with open('../input/15.txt') as f:
    maze = []
    for line in f:
        row = []
        for unit in line:
            hp = 200 if unit in ['E', 'G'] else 0
            row.append([unit, hp])
        maze.append(row)

adj_units = lambda x, y, maze: [maze[j][i][0] for i, j in neighbors(x, y)]
neighbors = lambda x, y: [(x+i, y+j) for i, j in ((0, -1), (-1, 0), (1, 0), (0, 1))]

def move(xi, yi, enemy, maze):
    seen, potential = set(), set()
    queue = [(xi+x, yi+y, i, 1, i) for i, (x, y) in enumerate(neighbors(0, 0)) if maze[yi+y][xi+x][0] == '.']
    for x, y, way, dist, step in queue:
        if enemy in adj_units(x, y, maze):
            potential.add((dist,) + neighbors(x, y)[3-way][::-1] + neighbors(0, 0)[step][::-1])
        children = [(x, y, i, dist+1, step) for i, (x, y) in enumerate(neighbors(x, y))]
        del children[3-way]
        for c_x, c_y, c_way, c_dist, c_step in children:
            if (c_x, c_y) not in seen and maze[c_y][c_x][0] == '.':
                queue.append((c_x, c_y, c_way, c_dist, c_step))
                seen.add((c_x, c_y))
    for dist, y, x, j, i in sorted(potential):
        return xi + i, yi + j
    return xi, yi

def play(maze, atk=3, end_if_elf_died=False):
    turn = 0
    while True:
        moved = set()
        for yi, row in enumerate(maze):
            for xi, (unit, hp) in enumerate(row):
                if unit not in ['E', 'G'] or (xi, yi) in moved:
                    continue
                alive_units = set([j[0] for i in maze for j in i if j[0] in ['E', 'G']])
                if len(alive_units) == 1:
                    result = turn * sum(sum(zip(*row)[1]) for row in maze)
                    return alive_units.pop(), result
                x, y = xi, yi
                enemy = 'G' if unit == 'E' else 'E'
                #for row in maze:
                    #print ''.join(zip(*row)[0])
                if enemy not in adj_units(x, y, maze):
                    maze[y][x] = ['.', 0]
                    x, y = move(x, y, enemy, maze)
                    maze[y][x] = [unit, hp]
                    moved.add((x, y))
                if enemy in adj_units(x, y, maze):
                    targets = sorted(neighbors(x, y), key = lambda (k, l): maze[l][k][1])
                    e_x, e_y = next(((i, j) for i, j in targets if maze[j][i][0] == enemy))
                    maze[e_y][e_x][1] -= 3 if unit == 'G' else atk
                    if maze[e_y][e_x][1] <= 0:
                        maze[e_y][e_x] = ['.', 0]
                        if end_if_elf_died and enemy == 'E':
                            return 'G', 0
        turn += 1

print play(deepcopy(maze))[1]

# only try those atk's which take a different amount of hits to kill a goblin
for atk in iter(set(map(lambda hits: int(ceil(200.0/hits)), range(200/4, 0, -1)))):
    winner, outcome = play(deepcopy(maze), atk, True)
    if winner == 'E':
        print outcome
        break
