import re
from collections import defaultdict
from copy import deepcopy


with open("../input/5.txt") as f:
    crates, moves = map(str.splitlines, f.read().rstrip().split("\n\n"))

*rows, column = crates
columns = defaultdict(list)
for row in reversed(rows):
    for i, crate in enumerate(row):
        if crate.isupper():
            columns[int(column[i])].append(crate)

columns2 = deepcopy(columns)
for move in moves:
    x, y, z = map(int, re.findall(r"\d+", move))
    for i in range(x):
        columns[z].append(columns[y][-i - 1])
        columns2[z].append(columns2[y][len(columns2[y]) - x + i])

    del columns[y][-x:]
    del columns2[y][-x:]

print("".join(columns[i].pop() for i in range(1, len(columns) + 1)))
print("".join(columns2[i].pop() for i in range(1, len(columns2) + 1)))
