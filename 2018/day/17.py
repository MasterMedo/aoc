clay, water, stillwater = set(), set(), set()
with open('../input/17.txt') as f:
    for l, r in map(str.split, f):
        a, b = map(int, r[2:].split('..'))
        for w in range(a, b + 1):
            if l[0] == 'x':
                clay.add((int(l[2:-1]), w))
            else:
                clay.add((w, int(l[2:-1])))

xmin, ymin = map(min, zip(*clay))
xmax, ymax = map(max, zip(*clay))

down, leftright = {(500, 0)}, set()
while down | leftright:
    while down:
        x, y = down.pop()
        if y > ymax:
            break
        water.add((x, y))
        if (x, y+1) in clay | stillwater:
            leftright.add((x, y))
        elif (x, y+1) not in water - stillwater:
            down.add((x, y+1))
    while leftright:
        x, y = leftright.pop()
        stream, spills = {(x, y)}, set()
        for way in [-1, 1]:
            i, j = x+way, y
            while (i, j) not in clay:
                stream.add((i, j))
                if (i, j+1) not in clay | stillwater:
                    spills.add((i, j))
                    break
                i += way
        if spills:
            water.update(stream)
            down.update(spills)
        if not spills:
            water.update(stream)
            stillwater.update(stream)
            leftright.add((x, y-1))

print len(water) - ymin
print len(stillwater)
