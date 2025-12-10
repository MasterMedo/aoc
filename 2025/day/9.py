def area(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


def position(x, y):
    return (
        next(i for i, n in enumerate(X) if len(n) == 1 and n[0] == x),
        next(i for i, n in enumerate(Y) if len(n) == 1 and n[0] == y)
    )


def area2(a, b):
    x1, y1 = position(*data[a])
    x2, y2 = position(*data[b])

    if any(not grid[i][j]
           for i in range(*sorted([y1, y2]))
           for j in range(*sorted([x1, x2]))):
        return 0

    return area(data[a], data[b])


with open("../input/9.txt") as f:
    data = [tuple(map(int, line.split(","))) for line in f.readlines()]

print(max(area(data[i], data[j]) for i in range(len(data)) for j in range(i, len(data))))

xs = sorted(set(x for x, _ in data))
ys = sorted(set(y for _, y in data))

X = [[xs[0]]]
for a, b in zip(xs[:-1], xs[1:]):
    X.append([a, b])
    X.append([b])

Y = [[ys[0]]]
for a, b in zip(ys[:len(ys)-1], ys[1:]):
    Y.append([a, b])
    Y.append([b])

grid = [[False for _ in range(len(X))] for _ in range(len(Y))]
data.append(data[0])
for (x, y), (a, b) in zip(data[:-1], data[1:]):
    flag = False
    if x == a:
        d = next(i for i, n in enumerate(X) if len(n) == 1 and n[0] == x)
        for i, n in enumerate(Y):
            if flag is True:
                grid[i][d] = True
            if len(n) == 1 and n[0] in (y, b):
                grid[i][d] = True
                if flag is True:
                    break
                flag = True
    else:
        d = next(i for i, n in enumerate(Y) if len(n) == 1 and n[0] == y)
        for i, n in enumerate(X):
            if flag is True:
                grid[d][i] = True
            if len(n) == 1 and n[0] in (x, a):
                grid[d][i] = True
                if flag is True:
                    break
                flag = True

seen = set()
x, y = position(*data[0])
visit = [(x - 1, y + 1)]
while visit:
    x, y = visit.pop()
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        p = nx, ny = x + dx, y + dy
        if p not in seen and grid[ny][nx] is not True:
            grid[ny][nx] = True
            seen.add(p)
            visit.append(p)

print(max(area2(i, j) for i in range(len(data)) for j in range(i, len(data))))
