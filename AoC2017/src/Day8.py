from collections import defaultdict

with open("../inputs/Day8_input.txt") as f:
  data = f.read().strip()

m = 0
d = defaultdict(int)
data += '\n'
data = data.replace('\n', ' else 0\n')
data = data.replace('inc', '+=')
data = data.replace('dec', '-=')
for line in data.splitlines():
  exec(line, {}, d)
  if m < max(d.values()):
    m = max(d.values())
print max(d.values())
print m