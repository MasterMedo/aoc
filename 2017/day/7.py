with open("../input/7.txt") as f:
  data = [i.replace(',', '').split() for i in f.readlines()]

part1 = set(i[0] for i in data).difference(set(j for i in data for j in i[2:])).pop()
print part1

weight = {}
for i in xrange(len(data)):
    data[i][1] = int(data[i][1][1:-1])
    weight[data[i][0]] = data[i][1]
    
m = {part1: -float('inf')}
while m[part1] == -float('inf'):
    i = data.pop()
    above = [m.get(j, -float('inf')) for j in i[3:]]
    m[i[0]] = i[1] if len(i) == 2 else sum(above) + i[1]
    if m[i[0]] == -float('inf'):
        data.insert(0, i)
    elif len(above) > 0 and above.count(above[0]) != len(above):
        node = [x for x in i[3:] if above.count(m[x]) == 1][0]
        print weight[node] + sum(set(above)) - 2 * m[node]
        break
