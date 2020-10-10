with open('../input/1.txt') as f:
    data = f.read().strip().split(', ')

zw = None
xy = angle = 0
visited = set()
for direction, *steps in data:
    angle += 1 if direction == 'R' else -1
    for _ in range(int(''.join(steps))):
        xy += 1j**angle
        if zw is None and xy in visited:
            zw = xy
        visited.add(xy)

print(int(abs(xy.real) + abs(xy.imag)))
print(int(abs(zw.real) + abs(zw.imag)))
