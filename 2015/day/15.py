from operator import mul

def prod(iterable):
    return reduce(mul, iterable, 1)

def org(x):
    x = x.replace(',','').split()
    return x[0][:-1], [int(x[2]), int(x[4]), int(x[6]), int(x[8]), int(x[-1])]

with open('../input/15.txt') as fp:
    data = dict([org(x) for x in fp.read().strip().splitlines()])

m, c = 0, 0
for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101):
            for l in range(0, 101):
                if i + j + k + l == 100:
                    s = [sum([data[x][z] * y for x, y in zip(data, [i, j, k, l])]) for z in range(4)]
                    if min(s) > 0:
                        m = max(m, prod(s))
                        if sum([data[x][-1] * y for x, y in zip(data, [i, j, k, l])]) == 500:
                            c = max(c, prod(s))

print m
print c
