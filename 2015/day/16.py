def org(i):
    i = i.replace(':','').replace(',','').split()
    return int(i[1]), {x: int(y) for x,y in zip(i[2::2], i[3::2])}

with open('../input/16.txt') as fp:
    data = dict([org(i) for i in fp.read().strip().splitlines()])

with open('../input/16-ticker-tape.txt') as f:
    tt = {y: int(z) for x in f.read().strip().splitlines() for y, z in [x.replace(':', '').split()]}

for i in data:
    for j in tt:
        if j in data[i] and tt[j] != data[i][j]:
            break
    else:
        print i

for i in data:
    for j in tt:
        if j in data[i] and \
        (j not in ('cats', 'trees', 'pomerians', 'goldfish') and tt[j] != data[i][j] or \
        j in ('cats', 'trees') and tt[j] >= data[i][j] or \
        j in ('pomeranians', 'goldfish') and tt[j] <= data[i][j]):
            break
    else:
        print i

