with open('../input/10.txt') as fp:
    data = [int(i) for i in list(fp.read().strip())]

# for i in range(40):
for i in range(50):
    tmp, cur, cnt = [], data[0], 0
    for i in data:
        if i != cur:
            tmp.extend([cnt, cur])
            cnt, cur = 0, i
        cnt += 1
    tmp.extend([cnt, cur])
    data = tmp

print len(data)
