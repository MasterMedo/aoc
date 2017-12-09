def getWeight(key):
  if len(wAndn[key]) == 2:
    return wAndn[key][0]
  return sum([getWeight(x) for x in wAndn[key][2:]]) + wAndn[key][0]

with open("../inputs/Day7_input.txt") as f:
  rows = [line.replace(",", "").split() for line in f.read().strip().splitlines()]

# Part 1
nodes = []
potentials = []
for row in rows:
  potentials.append(row[0])
  i = len(row) - 1
  while row[i] != "->" and len(row) > 3:
    if row[i] not in nodes:
      nodes.append(row[i])
    i -= 1

for p in potentials:
  if p not in nodes:
    print p, "is the base node"

# Part 2
wAndn = {}
for row in rows:
  L = []
  L.append(int(row[1].replace(")","").replace("(","")))
  L.append(0)
  if len(row) > 3:
    L += [x for x in row[3:]]
  wAndn[row[0]] = L

for key in wAndn:
  wAndn[key][1] = getWeight(key)

faulty = []
potentials = []
for key in wAndn:
  if len(wAndn[key]) > 2:
    for i in wAndn[key][2:]:
      for j in wAndn[key][2:]:
        if wAndn[i][1] != wAndn[j][1]:
          for k in wAndn[key][2:]:
            if wAndn[k][1] != wAndn[i][1] and k != j:
              if i not in potentials:
                potentials.append(i)
                faulty.append(i)
for f in faulty:
  for i in wAndn[f][2:]:
    if i in faulty and f in potentials:
      potentials.remove(f)
node = potentials[0]
for f in faulty:
  if node in wAndn[f][2:]:
    for i in wAndn[f][2:]:
      if i != node:
        print "Weight of node", node, "should be", wAndn[node][0] + wAndn[i][1] - wAndn[node][1]
        break
