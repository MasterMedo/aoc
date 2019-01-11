from itertools import count

track, cars, orientation = {}, {}, '>v<^'
with open('../input/13.txt') as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, c in enumerate(row):
            track[x + y*1j] = c
            if c in orientation:
                track[x + y*1j] = '-' if c in '<>' else '|'
                cars[x + y*1j] = (orientation.index(c), 0)

for tick in count():
    for xy in sorted(cars, key = lambda i: (i.imag, i.real)):
        if xy not in cars:
            continue
        c, (w, t) = track[xy], cars.pop(xy) # w=way, t=turn
        if c == '+':
            w = (t-1)**2*(w+t-1)%4 + (2*t-t**2)*w
            t = (t+1)%3
        if c in '/\\':
            w = 3-w if c == '/' else 3*w-3
        xy += 1j**w
        if xy in cars:
            cars.pop(xy)
            print 'crash ' + str(xy)
            continue
        cars.update({xy: (w, t)})
    if len(cars) == 1:
        print 'winner ' + str(set(cars).pop())
        break
