from heapq import heappush, heappop


def bfs(grid, char):
    visit = []
    seen = {}
    for start in grid:
        if grid[start] in char:
            heappush(visit, (0, *start))
            seen[start] = 0

    while visit:
        d, x, y = heappop(visit)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            z = x + dx
            w = y + dy
            if (z, w) not in seen and (z, w) in grid:
                a = grid[x, y] if grid[x, y] != "S" else "a"
                b = grid[z, w] if grid[z, w] != "E" else "z"
                if ord(a) + 1 < ord(b):
                    continue
                seen[z, w] = d + 1
                if grid[z, w] == "E":
                    return d + 1
                heappush(visit, (d + 1, z, w))


with open("../input/12.txt") as f:
    grid = {(x, y): c for y, line in enumerate(f) for x, c in enumerate(line.strip())}

print(bfs(grid, "S"))
print(bfs(grid, "aS"))
