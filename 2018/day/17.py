import re

clay, water, stillwater = set(), set(), set()
with open('../input/17.txt') as f:
    for line in f:
        x, a, b = map(int, re.findall(r'\d+', line))
        for y in range(a, b+1):
            clay.add((x, y) if line[0] == 'x' else (y, x))

xmin, ymin = map(min, zip(*clay))
xmax, ymax = map(max, zip(*clay))

down, leftright = {(500, 0)}, set()
while down or leftright:
    while down:
        x, y = down.pop()
        while y <= ymax and (x, y) not in water:
            water.add((x,y))
            if (x, y+1) in clay or (x, y+1) in stillwater:
                leftright.add((x, y))
                break
            y += 1

    while leftright:
        x, y = leftright.pop()
        water.add((x, y))
        spills = False
        stream = {(x, y)}
        for way in [-1, 1]:
            i, j = x+way, y
            while (i, j) not in clay:
                stream.add((i, j))
                if (i, j+1) not in clay and (i, j+1) not in stillwater:
                    down.add((i, j))
                    spills = True
                    break
                water.add((i, j))
                i += way

        if not spills:
            stillwater.update(stream)
            leftright.add((x, y-1))

print(len(water) - ymin)
print(len(stillwater))
