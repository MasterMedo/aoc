from collections import defaultdict


with open("../input/18.txt") as f:
    lines = f.read().strip().split("\n")

grid = set()
max_x = 0
max_y = 0
max_z = 0
for line in lines:
    x, y, z = map(int, line.split(","))
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    max_z = max(max_z, z)
    grid.add((x, y, z))


neighbours = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]
score = 0
border = set()
for x in range(-2, max_x + 2):
    for y in range(-2, max_y + 2):
        for z in range(-2, max_z + 2):
            if (x, y, z) not in grid:
                for dx, dy, dz in neighbours:
                    if (x + dx, y + dy, z + dz) in grid:
                        border.add((x + dx, y + dy, z + dz))
                        score += 1

print(score)
to_visit = [(-2, -2, -2)]
seen = set()
exterior = defaultdict(int)
while to_visit:
    x, y, z = to_visit.pop()
    for dx, dy, dz in neighbours:
        point = (nx, ny, nz) = x + dx, y + dy, z + dz
        if (
            nx < -2
            or nx > max_x + 2
            or ny < -2
            or ny > max_y + 2
            or nz < -2
            or nz > max_z + 2
        ):
            continue
        if point in border:
            exterior[point] += 1
        elif point not in seen:
            seen.add(point)
            to_visit.append(point)

print(sum(exterior.values()))
