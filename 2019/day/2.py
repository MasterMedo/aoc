with open('../input/2.txt') as f:
    data = list(map(int, f.read().split(',')))

def run(l, i, j):
    l[1], l[2] = i, j
    for i in range(0, len(l), 4):
        if l[i] == 99:
            return l[0]
        a, b = l[l[i+1]], l[l[i+2]]
        l[l[i+3]] = a + b if l[i] == 1 else a * b

print(run(data[:], 12, 2))
print(next(100*i+j for i in range(100)
    for j in range(100) if run(data[:], i, j) == 19690720))
