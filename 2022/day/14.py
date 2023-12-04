from itertools import pairwise
from collections import defaultdict

with open("../input/14.txt") as f:
    data = f.read().rstrip().split("\n")

grid = defaultdict(lambda: ".")
for line in data:
    arr = line.split(" -> ")
    for a, b in pairwise(arr):
        x, y = map(int, a.split(","))
        z, w = map(int, b.split(","))
        x, z = sorted((x, z))
        y, w = sorted((y, w))
        if x == z:
            for i in range(y, w + 1):
                grid[x, i] = "#"
        elif y == w:
            for i in range(x, z + 1):
                grid[i, y] = "#"
        else:
            print("error")

lowest_point = max((y for x, y in grid)) + 2
leftmost = min((x for x, y in grid)) - 1000
rightmost = max((x for x, y in grid)) + 1000
for x in range(leftmost, rightmost):
    grid[x, lowest_point] = "#"
while True:
    sx, sy = 500, 0
    while sy <= lowest_point:
        if grid[sx, sy + 1] in "#o":
            if grid[sx - 1, sy + 1] not in "#o":
                sx -= 1
            elif grid[sx + 1, sy + 1] not in "#o":
                sx += 1
            else:
                if sx == 500 and sy == 0:
                    print(sum(v == "o" for v in grid.values()) + 1)
                    exit("done 1")
                grid[sx, sy] = "o"
                break
        sy += 1
    else:
        print(sum(v == "o" for v in grid.values()))
        exit("done 2")
