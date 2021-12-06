from collections import defaultdict

d = defaultdict(int)
with open("../input/6.txt") as f:
    for n in f.read().split(","):
        d[int(n)] += 1

for days_passed in range(256):
    d2 = {i: d[i + 1] for i in range(8)}
    d2[6] += d[0]
    d2[8] = d[0]
    d = d2
    if days_passed == 79:
        print(sum(d.values()))

print(sum(d.values()))
