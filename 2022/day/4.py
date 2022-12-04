with open("../input/4.txt") as f:
    data = f.read().strip().split("\n")


p1 = 0
p2 = 0
for line in data:
    a, b = line.split(",")
    x, y = map(int, a.split("-"))
    z, w = map(int, b.split("-"))

    if x >= z and y <= w or z >= x and w <= y:
        p1 += 1

    if max(x, z) <= min(y, w):
        p2 += 1

print(p1)
print(p2)
