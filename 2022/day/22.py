import re


def wrap(xy: complex, direction: complex) -> complex:
    zw = xy
    while zw in grid:
        zw -= pow(1j, direction)
    zw += pow(1j, direction)
    return xy if grid[zw] == "#" else zw


with open("../input/22.txt") as f:
    m, instructions = f.read().rstrip().split("\n\n")

grid = {}
xy = None
direction = 0
for y, line in enumerate(m.split("\n"), 1):
    for x, c in enumerate(line, 1):
        if c == "#":
            grid[x + y * 1j] = "#"
        elif c == ".":
            grid[x + y * 1j] = "."
            if xy is None:
                xy = x + y * 1j

for m in re.finditer(r"\d+", instructions):
    start, end = m.span()
    d = instructions[start - 1]
    n = instructions[start:end]
    if start != 0:
        direction = (direction + (1 if d == "R" else -1)) % 4
    for _ in range(int(n)):
        if xy + pow(1j, direction) not in grid:
            xy = wrap(xy, direction)
        elif grid[xy + pow(1j, direction)] == ".":
            xy += pow(1j, direction)
        elif grid[xy + pow(1j, direction)] == "#":
            pass

print(int(1000 * xy.imag + 4 * xy.real + direction))
