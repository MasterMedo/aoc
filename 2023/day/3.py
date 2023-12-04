import re

from collections import defaultdict

with open("../input/3.txt") as f:
    grid = f.read().split("\n")[:-1]

symbols = {}
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        symbols[r, c] = not char.isdigit() and char != "."

sum1 = 0
gears = defaultdict(list)
for r, row in enumerate(grid):
    for n in re.finditer("\d+", row):
        neighbours = [
            (r, c)
            for r in range(r - 1, r + 2)
            for c in range(n.start() - 1, n.end() + 1)
            if (r, c) in symbols and symbols[r, c]
        ]
        if neighbours:
            sum1 += int(n.group())

        for y, x in neighbours:
            if grid[y][x] == "*":
                gears[y, x].append(int(n.group()))

print(sum1)
print(sum(nums[0] * nums[1] for nums in gears.values() if len(nums) == 2))
