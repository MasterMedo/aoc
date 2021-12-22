import re
from itertools import chain
from bisect import bisect

with open("../input/22.txt") as f:
    data = f.read()[:-1].split("\n")

cuboids = []
for line in data:
    on, other = line.split()
    xmin, xmax, ymin, ymax, zmin, zmax = map(int, re.findall(r"-?\d+", other))
    cuboids.append((on, xmin, xmax + 1, ymin, ymax + 1, zmin, zmax + 1))

_, xmins, xmaxs, ymins, ymaxs, zmins, zmaxs = zip(*cuboids)
X = sorted(set(chain(xmins, xmaxs)))
Y = sorted(set(chain(ymins, ymaxs)))
Z = sorted(set(chain(zmins, zmaxs)))

XA = X[:]
YA = Y[:]
ZA = Z[:]
for i in range(len(X) - 1, 0, -1):
    X[i] -= X[i - 1]
for i in range(len(Y) - 1, 0, -1):
    Y[i] -= Y[i - 1]
for i in range(len(Z) - 1, 0, -1):
    Z[i] -= Z[i - 1]

small_space = set()
space = set()
for on, xmin, xmax, ymin, ymax, zmin, zmax in cuboids:
    for x in range(bisect(XA, xmin) , bisect(XA, xmax)):
        for y in range(bisect(YA, ymin) , bisect(YA, ymax)):
            for z in range(bisect(ZA, zmin),bisect(ZA, zmax)):
                if on == "on":
                    space.add((x, y, z))
                else:
                    space.discard((x, y, z))

    if (
        xmin >= -50
        and xmax <= 50
        and ymin >= -50
        and ymax <= 50
        and zmin >= -50
        and zmax <= 50
    ):
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                for z in range(zmin, zmax):
                    if on == "on":
                        small_space.add((x, y, z))
                    else:
                        small_space.discard((x, y, z))

print(len(small_space))
print(sum(X[x] * Y[y] * Z[z] for x, y, z in space))
