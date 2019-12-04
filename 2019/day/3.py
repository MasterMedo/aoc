with open('../input/3.txt') as f:
    data = [s.split(',') for s in f.read().split('\n')[:-1]]

wire = [dict(), dict()]
for i, w in enumerate(data):
    x = y = z = 0
    for j in w:
        for _ in range(int(j[1:])):
            if j[0] in 'LR':
                x += 1 if j[0] == 'R' else -1
            else:
                y += 1 if j[0] == 'U' else -1
            wire[i][(x, y)] = z
            z += 1

cross = set(wire[0]).intersection(set(wire[1]))
print(sorted(abs(x[0]) + abs(x[1]) for x in cross)[0])
print(sorted(wire[0][x]+wire[1][x] for x in cross)[0]+2)
