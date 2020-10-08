from hashlib import md5
from heapq import heappush, heappop


with open('../input/17.txt') as f:
    code = f.read()[:-1]

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
letters = 'UDLR'
to_visit = [(0, 0, 0, code)]
first = last = None

while to_visit:
    distance, x, y, code = heappop(to_visit)

    if x == y == 3:
        if first is None:
            first_solution = code[8:]
        last = len(code) - 8
        continue

    for i, c in enumerate(md5(code.encode()).hexdigest()[:4]):
        if c in 'cbdef':
            x_, y_ = x + d[i][0], y + d[i][1]
            if 4 > x_ > -1 and 4 > y_ > -1:
                heappush(to_visit, (distance+1, x_, y_, code + letters[i]))

print(last)
