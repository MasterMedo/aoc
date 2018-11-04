def org(i):
    i = i.replace(':', '').replace(',', '').split()
    return int(i[1]), {x: int(y) for x,y in zip(i[2::2], i[3::2])}

with open('../input/16.txt') as f, open('../input/16-ticker-tape.txt') as ftt:
    data = dict(org(i[:-1]) for i in f.readlines())
    tt = {y: int(z) for x in ftt.readlines() for y, z in [x.replace(':', '').split()]}

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

