def org(l):
    l[0] = l[0].split()
    if len(l[0]) == 1:
        return l[1], [lambda a, b: get(a), l[0][0], None]
    return l[1], [f[l[0][-2]], l[0][0], l[0][-1]]

def get(key):
    if key not in m and (isinstance(key, int) or key.isdigit()):
        m[key] = int(key)
    elif key not in m:
        m[key] = data[key][0](data[key][1], data[key][-1]) 
    return m[key]

f = { 
        'NOT'   : lambda a, b: ~ get(b),
        'AND'   : lambda a, b: get(a) & get(b),
        'OR'    : lambda a, b: get(a) | get(b),
        'RSHIFT': lambda a, b: get(a) >> get(b),
        'LSHIFT': lambda a, b: get(a) << get(b),
    }

with open('../input/7.txt') as fp:
    data = dict([org(i[:-1].split(' -> ')) for i in fp.readlines()])

m = {}
firstPart, m = get('a'), {}
data['b'] = [lambda a, b: get(a), firstPart, None]

print firstPart
print get('a')
