with open("../input/7.txt") as f:
    grid = [[char for char in line.strip()] for line in f.readlines()]

split = 0
start = (0, next(c for c, char in enumerate(grid[0]) if char == "S"))
seen = {start: 1}
visit = [start]
while visit:
    r, c = visit.pop(0)
    n = seen[r, c]

    if len(grid) > r + 1:
        if grid[r+1][c] == "^":
            if len(grid[0]) > c:
                if (r+1, c+1) not in seen:
                    seen[r+1, c+1] = n
                    visit.append((r+1, c+1))
                else:
                    seen[r+1, c+1] += n
            if c - 1 >= 0:
                if (r+1, c-1) not in seen:
                    seen[r+1, c-1] = n
                    visit.append((r+1, c-1))
                else:
                    seen[r+1, c-1] += n
            split += 1
        elif grid[r+1][c] != "|":
            if (r+1, c) not in seen:
                seen[r+1, c] = n
                visit.append((r+1, c))
            else:
                seen[r+1, c] += n

print(split)
print(sum(seen.get((len(grid)-1, c), 0) for c in range(len(grid[0]))))
