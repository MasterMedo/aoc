def solve(c, x, n):
    return n if len(c) == 0 else max([solve(c.difference({y}), y, n + data.get((x, y), data.get((y, x), 0))) for y in c])
    return n if len(c) == 0 else min([solve(c.difference({y}), y, n + data.get((x, y), data.get((y, x), 0))) for y in c])

with open('../input/09.txt') as fp:
    data = dict([((i.split()[0], i.split()[2]), int(i.split()[4])) for i in fp.read().strip().splitlines()])

cities = {city for pair in data for city in pair}
print solve(cities, 'anything', 0)
