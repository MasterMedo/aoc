from copy import deepcopy
from collections import deque

with open('../input/24.txt') as f:
    grid = [[c for c in line[:-1]] for line in f]

start = deepcopy(grid)
visited = set()
while (tmp := tuple(tuple(sublist) for sublist in grid)) not in visited:
    visited.add(tmp)
    grid_ = deepcopy(grid)
    for y, row in enumerate(grid_):
        for x, c in enumerate(row):
            bugs = sum(grid_[w][z] == '#'
                       for z, w in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                       if 0 <= z < 5 and 0 <= w < 5)

            if c == '#' and bugs != 1:
                grid[y][x] = '.'

            elif c == '.' and bugs == 1 or bugs == 2:
                grid[y][x] = '#'

print(sum(pow(2, i) for i, c in enumerate(c for row in grid for c in row)
          if c == '#'))

empty = [['.'] * 5 for _ in range(5)]
grid = deque([start])
for i in range(200):
    if i % 2 == 0:
        grid.append(deepcopy(empty))
        grid.appendleft(deepcopy(empty))

    grid_ = deepcopy(grid)
    for z, matrix in enumerate(grid_):
        for y, row in enumerate(matrix):
            for x, c in enumerate(row):
                if x == 2 and y == 2:
                    continue

                elif x == 0 and y == 0:
                    bugs = [[0, 1, z], [1, 0, z], [1, 2, z+1], [2, 1, z+1]]

                elif x == 1 and y == 0:
                    bugs = [[0, 0, z], [1, 1, z], [2, 0, z], [2, 1, z+1]]

                elif x == 2 and y == 0:
                    bugs = [[1, 0, z], [2, 1, z], [3, 0, z], [2, 1, z+1]]

                elif x == 3 and y == 0:
                    bugs = [[2, 0, z], [3, 1, z], [4, 0, z], [2, 1, z+1]]

                elif x == 4 and y == 0:
                    bugs = [[3, 0, z], [4, 1, z], [3, 2, z+1], [2, 1, z+1]]

                elif x == 0 and y == 1:
                    bugs = [[0, 0, z], [1, 1, z], [0, 2, z], [1, 2, z+1]]

                elif x == 1 and y == 1:
                    bugs = [[1, 0, z], [2, 1, z], [1, 2, z], [0, 1, z]]

                elif x == 2 and y == 1:
                    bugs = [[2, 0, z], [3, 1, z], [1, 1, z],
                            *[[i, 0, z-1] for i in range(5)]]

                elif x == 3 and y == 1:
                    bugs = [[3, 0, z], [4, 1, z], [3, 2, z], [2, 1, z]]

                elif x == 4 and y == 1:
                    bugs = [[4, 0, z], [3, 1, z], [4, 2, z], [3, 2, z+1]]

                elif x == 0 and y == 2:
                    bugs = [[0, 1, z], [0, 3, z], [1, 2, z], [1, 2, z+1]]

                elif x == 1 and y == 2:
                    bugs = [[1, 1, z], [1, 3, z], [0, 2, z],
                            *[[0, i, z-1] for i in range(5)]]

                elif x == 3 and y == 2:
                    bugs = [[3, 1, z], [3, 3, z], [4, 2, z],
                            *[[4, i, z-1] for i in range(5)]]

                elif x == 4 and y == 2:
                    bugs = [[4, 1, z], [4, 3, z], [3, 2, z], [3, 2, z+1]]

                elif x == 0 and y == 3:
                    bugs = [[0, 2, z], [0, 4, z], [1, 3, z], [1, 2, z+1]]

                elif x == 1 and y == 3:
                    bugs = [[1, 2, z], [1, 4, z], [2, 3, z], [0, 3, z]]

                elif x == 2 and y == 3:
                    bugs = [[2, 4, z], [3, 3, z], [1, 3, z],
                            *[[i, 4, z-1] for i in range(5)]]

                elif x == 3 and y == 3:
                    bugs = [[3, 2, z], [3, 4, z], [4, 3, z], [2, 3, z]]

                elif x == 4 and y == 3:
                    bugs = [[4, 2, z], [4, 4, z], [3, 3, z], [3, 2, z+1]]

                elif x == 0 and y == 4:
                    bugs = [[0, 3, z], [1, 4, z], [1, 2, z+1], [2, 3, z+1]]

                elif x == 1 and y == 4:
                    bugs = [[1, 3, z], [0, 4, z], [2, 4, z], [2, 3, z+1]]

                elif x == 2 and y == 4:
                    bugs = [[2, 3, z], [1, 4, z], [3, 4, z], [2, 3, z+1]]

                elif x == 3 and y == 4:
                    bugs = [[3, 3, z], [2, 4, z], [4, 4, z], [2, 3, z+1]]

                elif x == 4 and y == 4:
                    bugs = [[4, 3, z], [3, 4, z], [3, 2, z+1], [2, 3, z+1]]

                bugs = sum(grid_[z_][y_][x_] == '#' for x_, y_, z_ in bugs
                           if 0 <= z_ < len(grid))

                if c == '#' and bugs != 1:
                    grid[z][y][x] = '.'

                elif c == '.' and bugs == 1 or bugs == 2:
                    grid[z][y][x] = '#'

print(sum(c == '#' for c in c for mat in grid for row in mat for c in row))
