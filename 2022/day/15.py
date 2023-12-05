import re

with open("../input/15.txt") as f:
    data = f.read().strip().split("\n")

ranges = []
radiuses = {}
for line in data:
    x, y, z, w = map(int, re.findall(r"-?\d+", line))
    d = abs(x - z) + abs(y - w)
    radiuses[x, y] = d
    tmp = d - abs(y - 2000000)
    if tmp < 0:
        continue
    intersection = tmp - x
    if d != abs(x - intersection) + abs(y - 2000000):
        intersection = x - tmp
    intersection_right = 2*x - intersection
    if intersection > x:
        intersection, intersection_right = intersection_right, intersection
    new = []
    for i, (low, high) in enumerate(ranges):
        if intersection_right >= low and high >= intersection:
            intersection = min(intersection, low)
            intersection_right = max(intersection_right, high)
        else:
            new.append((low, high))
    new.append((intersection, intersection_right))
    ranges = new

print(sum(high - low for low, high in ranges))

a_coeffs, b_coeffs = set(), set()
for ((x, y), r) in radiuses.items():
    a_coeffs.add(y - x + r + 1)
    a_coeffs.add(y - x - r - 1)
    b_coeffs.add(x + y + r + 1)
    b_coeffs.add(x + y - r - 1)

for a in a_coeffs:
    for b in b_coeffs:
        x = (b - a) // 2
        y = (a + b) // 2
        if all(0 < c < 4000000 for c in (x, y)):
            if all(abs(x - x2) + abs(y - y2) > r for (x2, y2), r in radiuses.items()):
                print(4000000 * x + y)
