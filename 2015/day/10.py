with open('../input/10.txt') as f:
    data = map(int, list(f.read().strip()))

for i in xrange(50): # 40
    tmp, cur, cnt = [], data[0], 0
    for i in data:
        if i != cur:
            tmp.extend([cnt, cur])
            cnt, cur = 0, i
        cnt += 1
    tmp.extend([cnt, cur])
    data = tmp

print len(data)
