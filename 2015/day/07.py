from ctypes import c_ushort

def get(key):
    global data, m
    if key in m:
        return m[key]
    try:
        m[key] = int(key)
        return m[key]
    except Exception:
        l = data[key]
        m[key] = l[0](l[-2], l[-1]) 
        return m[key]

def organize(l):
    global f
    l = l.split()
    for i in f:
        if i in l:
            return [f[i], l[0], l[-3]]
    return [lambda a, b: get(a), l[0], None]

m = {}
f = { 
        'NOT'   : lambda a, b: ~get(b),\
        'AND'   : lambda a, b: get(a)&get(b),\
        'OR'    : lambda a, b: get(a)|get(b),\
        'RSHIFT': lambda a, b: get(a)>>get(b),\
        'LSHIFT': lambda a, b: get(a)<<get(b),\
    }

with open('../input/07.txt') as fp:
    data = {l.split()[-1]: organize(l) for l in fp.read().strip().splitlines()}

firstPart=get('a')
print(c_ushort(firstPart))
m={}
data['b']=[lambda a, b: get(a), firstPart, None]
print(c_ushort(get('a')))
