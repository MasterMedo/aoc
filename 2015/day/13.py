def org(i):
    i = i[:len(i)-1].split()
    return (i[0], i[-1]), int(i[3]) if i[2] == 'gain' else -int(i[3])

def solve(x, c, n):
    if len(c) == 0:
        return n + data[x, item]
    s = 0
    for y in c:
        s = max(solve(y, c.difference({y}), n + data[x, y]), s)
    return s

with open('../input/13.txt') as fp:
    tmp = dict([org(i) for i in fp.read().strip().splitlines()])
    data = {(i, j): tmp[i, j] + tmp[j, i] for i, j in tmp}

p = {j for i in data for j in i}
# data.update({j: 0 for i in p for j in [('me', i), (i,'me')]})
# p = p.union({'me'})

item = p.pop()
print solve(item, p, 0)

