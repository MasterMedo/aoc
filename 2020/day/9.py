from collections import deque
from itertools import combinations

with open('../input/9.txt') as f:
    data = list(map(int, f))

for i, x in enumerate(data[25:], 25):
    if data[i] not in map(sum, combinations(data[i-25:i], 2)):
        print(data[i])
        break

s = 0
contiguous_set = deque()
for i, n in enumerate(data):
    if s == x and len(contiguous_set) > 1:
        print(min(contiguous_set) + max(contiguous_set))
        break

    contiguous_set.append(n)
    s += n
    while s > x:
        tmp = contiguous_set.popleft()
        s -= tmp
