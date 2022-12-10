from more_itertools import before_and_after
from functools import partial


with open("../input/8.txt") as f:
    rows = [[int(c) for c in line.strip()] for line in f.readlines()]
    cols = list(zip(*rows))

part1 = 0
for r in range(len(rows)):
    for c in range(len(cols)):
        tree = rows[r][c]
        part1 += (
            all(x < rows[r][c] for x in rows[r][:c])
            or all(x < rows[r][c] for x in rows[r][c + 1 :])
            or all(x < rows[r][c] for x in cols[c][:r])
            or all(x < rows[r][c] for x in cols[c][r + 1 :])
        )

max_score = 0
for r in range(len(rows)):
    for c in range(len(cols)):
        up = cols[c][:r][::-1]
        down = cols[c][r + 1 :]
        left = rows[r][:c][::-1]
        right = rows[r][c + 1 :]

        score = 1
        lower_and_higher = partial(before_and_after, lambda x: x < rows[r][c])
        for row in [up, down, left, right]:
            lower, higher = map(len, map(list, lower_and_higher(row)))
            score *= lower + bool(higher)

        if score > max_score:
            max_score = score

print(part1)
print(max_score)
