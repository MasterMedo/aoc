def org(line):
    l = line.split()
    return [((l[0], l[2]), int(l[4])), ((l[2], l[0]), int(l[4]))]

def solve(c, x, n):
    if len(c) == 0:
        return n
    #s = float('inf')
    s = 0
    for y in c:
        #s = min(solve(c.difference({y}), y, n + data[x, y]), s)
        s = max(solve(c.difference({y}), y, n + data[x, y]), s)
    return s

with open('../input/09.txt') as fp:
    data = dict([j for i in fp.read().strip().splitlines() for j in org(i)])

cities = {city for pair in data for city in pair}
for i in cities:
    data['any', i] = 0

print solve(cities, 'any', 0)
