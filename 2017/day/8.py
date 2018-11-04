from collections import defaultdict

with open("../input/8.txt") as f:
  data = f.read().replace('\n', ' else 0\n').replace('inc', '+=').replace('dec', '-=')

m, d = 0, defaultdict(int)
for line in data.splitlines():
    exec(line, {}, d)
    m = max(m, max(d.values()))

print max(d.values())
print m
