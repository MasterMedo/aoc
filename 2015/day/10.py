def exp(x):
    s, y, z = [], x[0], 0
    for i in x:
        if i != y:
            s.append(z)
            s.append(y)
            z = 0
            y = i
        z += 1
    s.append(z)
    s.append(y)
    return s

with open('../input/10.txt') as fp:
    data = [int(i) for i in list(fp.read().strip())]

# for i in range(40):
for i in range(50):
    data = exp(data)

print len(data)
