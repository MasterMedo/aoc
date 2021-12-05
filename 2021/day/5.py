from collections import defaultdict

with open("../input/5.txt") as f:
    data = f.readlines()

d = defaultdict(int)
d2 = defaultdict(int)
for line in data:
    a, b = line.split('->')
    x1, y1 = map(int, a.split(','))
    x2, y2 = map(int, b.split(','))
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            d[x1, i] += 1
            d2[x1, i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            d[i, y1] += 1
            d2[i, y1] += 1
    else:
        a = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        b = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        for x, y in zip(a, b):
            d2[x, y] += 1

print(sum(x > 1 for x in d.values()))
print(sum(x > 1 for x in d2.values()))
