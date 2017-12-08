def getWeight(key):
  if len(wAndn[key]) == 2:
    return wAndn[key][0]
  return sum([getWeight(x) for x in wAndn[key][2:]]) + wAndn[key][0]

with open("../inputs/Day7_input.txt") as f:
  rows = [line.replace(",", "").split() for line in f.read().strip().splitlines()]

wAndn = {}
for row in rows:
  L = []
  L.append(int(row[1].replace(")","").replace("(","")))
  L.append(0)
  if len(row) > 3:
    L+=[x for x in row[3:]]
  wAndn[row[0]] = L

for key in wAndn:
  wAndn[key][1] = getWeight(key)

for key in wAndn:
  if len(wAndn[key]) > 2:
    for i in wAndn[key][3:]:
      if wAndn[wAndn[key][2]][1] != wAndn[i][1]:
        break;

nodes = []
potentials = []
for row in rows:
  potentials.append(row[0])
  i = len(row)-1
  while row[i] != "->" and len(row) > 3:
    if row[i] not in nodes:
      nodes.append(row[i])
    i -= 1

for p in potentials:
  if p not in nodes:
    print p, "is the base node"
