def getn(data):
    return sum(data[x][y] for x in xrange(i - 1, i + 2) for y in xrange(j - 1, j + 2) \
            if (x != i or y != j) and x >= 0 and y >= 0 and x < 100 and y < 100)

def setc(data):
    for i in [0, 99]:
        for j in [0, 99]:
            data[i][j] = 1
    return data

with open('../input/18.txt') as fp:
    data = [map(int, list(i[:-1].replace('#', '1').replace('.', '0'))) for i in fp.readlines()]

data = setc(data)
for z in xrange(100):
    tmp = [[0 for y in xrange(100)] for x in xrange(100)]
    for i in xrange(100):
        for j in xrange(100):
            n = getn(data)
            tmp[i][j] = 0 if data[i][j] == 1 and n not in [2, 3] else data[i][j]
            tmp[i][j] = 1 if data[i][j] == 0 and n == 3 else tmp[i][j]
    # data = tmp
    data = setc(tmp)

print sum(j for i in data for j in i)
