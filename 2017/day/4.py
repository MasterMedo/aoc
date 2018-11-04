with open('../input/4.txt') as f:
    data = [i.split() for i in f.readlines()]

print sum(1 for i in data if len(i) == len(set(i)))
print sum(1 for i in data if len(i) == len(set(i))
        and all(j == k or set(j) != set(k) for j in i for k in i))
