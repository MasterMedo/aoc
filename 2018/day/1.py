from itertools import cycle, accumulate
data = list(map(int, open('../input/1.txt').readlines()))

seen = set([0])
print(sum(data))
print(next(f for f in accumulate(cycle(data)) if f in seen or seen.add(f)))
