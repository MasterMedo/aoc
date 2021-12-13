with open("../input/13.txt") as f:
    points, folds = f.read().split("\n\n")
    points = {tuple(map(int, line.split(","))) for line in points.split("\n")}

    for i, line in enumerate(folds.split("\n")[:-1]):
        coordinate, n = line.split()[-1].split("=")
        n = int(n)
        coordinate = 0 if coordinate == "x" else 1
        for point in list(points):
            if point[coordinate] > n:
                points.remove(point)
                point = list(point)
                point[coordinate] = 2 * n - point[coordinate]
                points.add(tuple(point))

        if i == 0:
            print(len(points))

for y in range(max(list(zip(*points))[1]) + 1):
    for x in range(max(list(zip(*points))[0]) + 1):
        print("#" if (x, y) in points else " ", end="")

    print()
