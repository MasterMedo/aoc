with open('../input/04.txt') as fp:
    data = [i.split() for i in fp.readlines()]

print sum(1 for i in data if len(i) == len(set(i)))
print sum(1 for i in data if len(i) == len(set(i))
        and all(j == k or set(j) != set(k) for j in i for k in i))
