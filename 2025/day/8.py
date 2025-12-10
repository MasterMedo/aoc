from heapq import heappush, heappop, nlargest
from math import dist, prod


with open("../input/8.txt") as f:
    data = [list(map(int, line.split(","))) for line in f.readlines()]

distances = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        heappush(distances, (dist(data[i], data[j]), i, j))

circuits = [[i] for i in range(len(data))]
part1 = 1000
while True:
    d, i, j = heappop(distances)
    new = []
    circuits2 = []
    for old in circuits:
        for k in old:
            if k == i or k == j:
                new.extend(old)
                break
        else:
            circuits2.append(old)
    circuits2.append(new)
    circuits = circuits2
    part1 -= 1
    if part1 == 0:
        print(prod(nlargest(3, map(len, circuits))))
    if len(circuits) == 1:
        print(data[i][0] * data[j][0])
        break
