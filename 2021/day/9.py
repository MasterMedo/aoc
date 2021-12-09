from collections import Counter

with open("../input/9.txt") as f:
    data = [list(map(int, line[:-1])) for line in f.readlines()]

part_1 = 0
basin = 0
seen = {}
stack = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if all(
            r + dr < 0
            or r + dr >= len(data)
            or c + dc < 0
            or c + dc >= len(data[0])
            or data[r][c] < data[r + dr][c + dc]
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0))
        ):
            part_1 += 1 + data[r][c]

        if (r, c) not in seen and data[r][c] != 9:
            stack.append((r, c))
            while stack:
                r, c = stack.pop()
                for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    r_ = r + dr
                    c_ = c + dc
                    if 0 <= r_ < len(data) and 0 <= c_ < len(data[0]):
                        if (r_, c_) not in seen and data[r_][c_] != 9:
                            seen[(r_, c_)] = basin
                            stack.append((r_, c_))
            basin += 1

print(part_1)
a, b, c = Counter(list(seen.values())).most_common(3)
print(a[1] * b[1] * c[1])
