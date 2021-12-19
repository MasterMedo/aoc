from itertools import starmap, cycle


negations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, -y, -z),
]

rotations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, x, y),
]

with open("../input/19.txt") as f:
    scanners = [
        set(tuple(map(int, line.split(","))) for line in chunk.split("\n")[1:])
        for chunk in f.read()[:-1].split("\n\n")
    ]

scanner_positions = [(0, 0, 0)] * len(scanners)
found = [-1] * len(scanners)
done = len(found) - 1
found[0] = 0
for i in cycle(range(len(scanners))):
    if done == 0:
        break

    if found[i] == -1:
        continue

    for j in range(len(scanners)):
        if j == i or found[j] != -1:
            continue

        for negate in negations:
            if found[j] != -1:
                break

            for rotate in rotations:
                if found[j] != -1:
                    break

                scanner_j = set(starmap(negate, starmap(rotate, scanners[j])))
                for x_1, y_1, z_1 in scanners[i]:
                    if found[j] != -1:
                        break
                    for x_2, y_2, z_2 in scanner_j:
                        if found[j] != -1:
                            break

                        dx, dy, dz = x_1 - x_2, y_1 - y_2, z_1 - z_2
                        moved = set(
                            (x + dx, y + dy, z + dz) for x, y, z in scanner_j
                        )

                        if len(scanners[i].intersection(moved)) >= 12:
                            scanners[j] = moved
                            found[j] = found[i]
                            scanner_positions[j] = (dx, dy, dz)
                            done -= 1
                            break

print(len(set.union(*scanners)))

max_distance = 0
for a, b, c in scanner_positions:
    for x, y, z in scanner_positions:
        max_distance = max(max_distance, abs(a - x) + abs(b - y) + abs(c - z))

print(max_distance)
