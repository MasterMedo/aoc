with open("../input/17.txt") as f:
    data = int(f.read())

L = [0]
pos = 0
for i in xrange(2017):
    pos = (pos + data) % len(L)
    L = L[:pos + 1] + [i + 1] + L[pos + 1:]
    pos += 1
print L[pos + 1]

l = 1
pos = 0
for i in xrange(50000000):
    pos = (pos + data) % l
    if pos == 0:
        part2 = i + 1
    l += 1
    pos += 1
print part2
