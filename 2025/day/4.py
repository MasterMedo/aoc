def isToiletPaper(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "@"


def neighbours(r, c):
    return sum(isToiletPaper(r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1))


grid = []
with open("../input/4.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

print(sum(grid[r][c] == "@" and neighbours(r, c) <= 4 for r in range(len(grid)) for c in range(len(grid[0]))))

s = 0
change = True
while change:
    change = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and neighbours(r, c) <= 4:
                grid[r][c] = "."
                s += 1
                change = True

print(s)
