from collections import defaultdict

with open("../input/10.txt") as f:
    grid = list(map(list, f.read().strip().split("\n")))

start = (0, 0)
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "S":
            up = r > 0 and grid[r - 1][c] in "7F|"
            left = c > 0 and grid[r][c - 1] in "-FL"
            down = r < len(grid) - 1 and grid[r + 1][c] in "|JL"
            right = c < len(grid[0]) - 1 and grid[r][c + 1] in "J7-"
            grid[r][c] = {
                (True, True, False, False): "J",
                (True, False, True, False): "|",
                (True, False, False, True): "L",
                (False, True, True, False): "7",
                (False, True, False, True): "-",
                (False, False, True, True): "F",
            }[up, left, down, right]
            start = (r, c)
            break
    else:
        continue
    break

distance = defaultdict(lambda: float("inf"))
distance[start] = 0
to_visit = [(*start, 0)]
while to_visit:
    r, c, d = to_visit.pop()
    # left
    if c > 0 and grid[r][c] in "-J7" and distance[r, c - 1] > d + 1 and grid[r][c - 1] in "-FL":
        distance[r, c - 1] = d + 1
        to_visit.append((r, c - 1, d + 1))
    # right
    if c < len(grid[0]) - 1 and grid[r][c] in "FL-" and distance[r, c + 1] > d + 1 and grid[r][c + 1] in "-7J":
        distance[r, c + 1] = d + 1
        to_visit.append((r, c + 1, d + 1))
    # up
    if r > 0 and grid[r][c] in "LJ|" and distance[r - 1, c] > d + 1 and grid[r - 1][c] in "|F7":
        distance[r - 1, c] = d + 1
        to_visit.append((r - 1, c, d + 1))
    # down
    if r < len(grid) - 1 and grid[r][c] in "|F7" and distance[r + 1, c] > d + 1 and grid[r + 1][c] in "|JL":
        distance[r + 1, c] = d + 1
        to_visit.append((r + 1, c, d + 1))

print(max(v for v in distance.values() if v != float("inf")))

nest_size = 0
for r, row in enumerate(grid):
    inside = False
    half_way = False
    for c, char in enumerate(row):
        if distance[r, c] != float("inf"):
            if char in "|":
                inside = not inside
            elif char in "FJL7":
                if half_way:
                    if half_way == "F" and char == "J" or half_way == "L" and char == "7":
                        inside = not inside
                    half_way = False
                else:
                    half_way = char
        elif inside:
            nest_size += 1

print(nest_size)
