def get(x):
    if type(x) == int or x.isdigit():
        power[x] = int(x)
    elif x not in power:
        function, a, b, = data[x]
        power[x] = function(a, b)
    return power[x]

def o(ins):
    if 'NOT'    in ins: return lambda a, b: ~ get(b)
    if 'AND'    in ins: return lambda a, b: get(a) & get(b)
    if 'OR'     in ins: return lambda a, b: get(a) | get(b)
    if 'RSHIFT' in ins: return lambda a, b: get(a) >> get(b)
    if 'LSHIFT' in ins: return lambda a, b: get(a) << get(b)
    else:               return lambda a, b: get(a)

with open('../input/7.txt') as f:
    data = {x: (o(i), i[0], i[-1]) for *i, _, x in map(str.split, f)}

power = {}
print(a := get('a'))
power = {'b': a}
print(get('a'))
