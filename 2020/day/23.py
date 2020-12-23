with open('../input/23.txt') as f:
    data = list(map(int, f.read().strip()))

size, iterations = 10**6, 10**7
d = list(range(1, size+2))
for i, e in enumerate(data[:-1]):
    d[e] = data[i+1]

d[data[-1]], d[size] = len(data) + 1, data[0]
label = data[0]
for _ in range(iterations):
    left = d[label]
    middle = d[left]
    right = d[middle]
    dest = (label - 2) % size + 1
    while dest in (left, middle, right):
        dest = (dest - 2) % size + 1

    d[label], d[dest], d[right] = d[right], left, d[dest]
    label = d[label]

print(d[1]*d[d[1]])
