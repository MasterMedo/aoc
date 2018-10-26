import json

def nsum(x):
    if isinstance(x, int):
        return x
    if isinstance(x, dict):
        if 'red' in x.values():
            return 0
    s = 0
    for i in x:
        if isinstance(x, (list, tuple)):
            s += nsum(i)
        elif isinstance(x, dict):
            s += nsum(x[i])
    return s

with open('../input/12.txt') as fp:
    data = json.load(fp)

print nsum(data)
