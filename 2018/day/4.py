from re import findall
from itertools import chain
from collections import defaultdict

data = [map(int, findall(r'\d+', i)) for i in sorted(open('../input/4.txt').readlines())]

asleep = -1
guards = defaultdict(lambda: [0 for i in range(60)])
for i in data:
    if len(i) == 6:
        gid = i[-1]
    else:
        asleep *= -1
        for j in range(i[4], 60):
            guards[gid][j] += asleep

p1 = max(map(sum, guards.values()))
p2 = max(chain(*guards.values()))

print next(gid * guards[gid].index(max(guards[gid])) for gid in guards if sum(guards[gid]) == p1)
print next(gid * guards[gid].index(p2) for gid in guards if p2 in guards[gid])
