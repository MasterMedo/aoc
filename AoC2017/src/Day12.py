with open("../inputs/p12.txt") as f:
  pipes = [line.replace('<->', '').replace(',','').split() for line in f.read().strip().splitlines()]

groups = []
for pipe in pipes:
  tmpS = set(pipe)
  tmpD = {}
  for i in range(len(groups)):
    if len(tmpS.intersection(groups[i])) > 0:
      tmpD[i] = groups[i]
  if len(tmpD) == 0:
    groups.append(tmpS)
  else:
    tmpA = []
    j = 0
    for i in tmpD:
      del groups[i-j]
      tmpA += tmpD[i]
      j += 1
    groups.append(set(tmpA).union(tmpS))

for group in groups:
  if '0' in group:
    print len(group)
print len(groups)
      
    
