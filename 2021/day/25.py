from itertools import count


def move(grid, char, func, moved):
    moved_grid = grid.copy()
    for x, y in grid:
        x_, y_ = func(x, y)
        if grid[x, y] == char and grid[x_, y_] == ".":
            moved_grid[x, y] = "."
            moved_grid[x_, y_] = char
            moved = True

    return moved_grid, moved


with open("../input/25.txt") as f:
    data = f.read().strip().split("\n")

grid = {(x, y): c for y, line in enumerate(data) for x, c in enumerate(line)}
X = max(x for x, _ in grid) + 1
Y = max(y for _, y in grid) + 1
for step in count(1):
    grid, moved = move(grid, ">", lambda x, y: ((x + 1) % X, y), False)
    grid, moved = move(grid, "v", lambda x, y: (x, (y + 1) % Y), moved)
    if not moved:
        print(step)
        break
