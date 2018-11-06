with open('../input/3.txt') as f:
    data = [map(int, i.split()) for i in f.readlines()]

print sum(1 for i in data if max(i) < sum(i) - max(i))
print sum(1 for i, j, k in zip(data[0::3], data[1::3], data[2::3])
        for l in zip(i, j, k) if max(l) < sum(l) - max(l))
