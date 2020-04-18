from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/19.txt') as f:
    tape = dict(enumerate(map(int, f.read().split(','))))

ray = lambda x, y: next(intcode(defaultdict(int, tape), iter([x, y])))

y, start = -1, 0
rows = {y: [start, start]}
while y <= 100 or rows[y-99][1] - start < 100:
    x = start
    y += 1
    if y == 50:
        x1, x2 = list(map(sum, zip(*rows.values())))
        print(x2 - x1)

    for _ in range(10): # taking care of empty rows
        if ray(x, y):
            break
        x += 1
    else:
        rows[y] = rows[y-1][:]
        if rows[y-1][1] > rows[y-1][0]: # if the row above is not empty
            rows[y][1] -= 1
        continue

    start = x
    x = max(start, rows[y-1][1])
    while ray(x, y):
        x += 1

    rows[y] = [start, x]

print(start*10000+y-99)
