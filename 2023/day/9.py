from collections import deque
from itertools import pairwise

s1 = 0
s2 = 0
with open("../input/9.txt") as f:
    for line in f:
        rows = [deque(map(int, line.split()))]
        while any(n != 0 for n in rows[-1]):
            rows.append(deque([b - a for a, b in pairwise(rows[-1])]))

        for i, row in enumerate(reversed(rows[1:])):
            rows[-i - 2].append(rows[-i - 2][-1] + row[-1])
            rows[-i - 2].appendleft(rows[-i - 2][0] - row[0])

        s1 += rows[0][-1]
        s2 += rows[0][0]

print(s1)
print(s2)
