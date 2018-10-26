def org(i):
    i = i.split()
    return (i[0], (int(i[3]), int(i[6]), int(i[-2])))

with open('../input/14.txt') as fp:
    data = dict([org(i) for i in fp.read().strip().splitlines()])

m, l, p = 2503, [], {x: [0, 0, 0] for x in data}
for i in data.values():
    l.append(i[0] * (-i[2] * ((m + i[2]) // (i[1] + i[2])) + m))
    
print max(l)

for i in range(m):
    for j in data:
        if p[j][2] <= -data[j][1]:
            p[j][2] = data[j][2]
        elif p[j][2] <= 0:
            p[j][1] += data[j][0]
        p[j][2] -= 1
    m = max([p[i][1] for i in p])
    for j in p:
        if p[j][1] == m:
            p[j][0] += 1

print max([p[i][0] for i in p])
