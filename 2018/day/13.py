from itertools import count

def move(xy, way, turn):
    c = track[xy]
    if c == '+':
        way = (way-1)%4 if turn == 0 else way if turn == 1 else (way+1)%4
        turn = (turn+1)%3
    if c in '/\\':
        way = 3-way if c == '/' else 3*way-3
    return xy + 1j**way, way, turn

track, cars, orientation = {}, {}, '>v<^'
with open('../input/13.txt') as f:
    for y, l in enumerate(f.read().splitlines()):
        for x, c in enumerate(l):
            track[x + y*1j] = c
            if c in orientation:
                track[x + y*1j] = '-' if c in '<>' else '|'
                cars[x + y*1j] = (orientation.index(c), 0)

for tick in count():
    for xy in sorted(cars, key = lambda ij: (ij.imag, ij.real)):
        if xy not in cars:
            continue
        xy, way, turn = move(xy, *cars.pop(xy))
        if xy in cars:
            cars.pop(xy)
            print 'crash '+str(xy)
            continue
        cars.update({xy: (way, turn)})
    if len(cars) == 1:
        print 'winner '+str(set(cars).pop())
        break
