def num(l, m, d):
    if m == 0:
        k.append(d)
        return 1
    s = 0
    for i in range(len(l)):
        s += num(l[i + 1:], m - l[i], d + 1)
    return s

with open('../input/17.txt') as f:
    data = [int(i) for i in f.readlines()]

k = []
print num(data, 150, 1)
print k.count(min(k))
