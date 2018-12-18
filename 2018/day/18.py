with open('../input/18.txt') as f:
    acres = {(x, y): c for y, l in enumerate(f.read().splitlines()) for x, c in enumerate(l)}

vals = []
adj = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]
for minute in xrange(1000000000):
    tmp = dict(acres)
    for y in xrange(50):
        for x in xrange(50):
            neighbors = [acres[x+i, y+j] for i, j in adj if (x+i, y+j) in acres]
            if acres[x, y] == '.' and neighbors.count('|') >= 3:
                tmp[x, y] = '|'
            elif acres[x, y] == '|' and neighbors.count('#') >= 3:
                tmp[x, y] = '#'
            elif acres[x, y] == '#' and not {'#', '|'} <= set(neighbors):
                tmp[x, y] = '.'
    if minute == 10:
        print acres.values().count('#') * acres.values().count('|')
    if minute >= 1000:
        result = acres.values().count('#') * acres.values().count('|')
        if result in vals:
            break
        vals.append(result)
    acres = dict(tmp)

print vals[999999000 % len(vals)]
