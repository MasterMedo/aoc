with open("../input/13.txt") as f:
    points, folds = f.read().strip().split("\n\n")

points = {tuple(map(int, line.split(","))) for line in points.split("\n")}
for i, line in enumerate(folds.split("\n")):
    coordinate, n = line.split()[-1].split("=")
    n = int(n)
    for x, y in list(points):
        points.remove((x, y))
        if coordinate == "x" and x > n:
            x = 2 * n - x

        if coordinate == "y" and y > n:
            y = 2 * n - y

        points.add((x, y))

    if i == 0:
        print(len(points))

X, Y = zip(*points)
for y in range(max(Y) + 1):
    for x in range(max(X) + 1):
        print(" #"[(x, y) in points], end="")

    print()
