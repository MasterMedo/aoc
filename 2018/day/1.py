from itertools import cycle
with open('../input/1.txt') as f:
    data = map(int, f)

print sum(data)
f, seen, gen = 0, set(), cycle(data)
while True:
    if f in seen:
        print f
        break
    seen.add(f)
    f += next(gen)


