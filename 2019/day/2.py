from operator import add, mul

with open('../input/2.txt') as f:
    data = list(map(int, f.read().split(',')))

def run(data, a, b):
    i, l = 0, data[:]
    l[1], l[2] = a, b
    op = lambda f: f(l[l[i+1]],l[l[i+2]])
    while True:
        if l[i] == 99:
            return l[0]
        l[l[i+3]] = op(add if l[i] == 1 else mul)
        i += 4

print(run(data, 12, 2))
print(next(100*a+b for a in range(100)
    for b in range(100) if run(data, a, b) == 19690720))
