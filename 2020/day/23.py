def emulate(d, label, iterations):
    for _ in range(iterations):
        left = d[label]
        middle = d[left]
        right = d[middle]
        dest = (label - 2) % size + 1
        while dest in (left, middle, right):
            dest = (dest - 2) % size + 1

        d[label], d[dest], d[right] = d[right], left, d[dest]
        label = d[label]
    return d


with open('../input/23.txt') as f:
    data = list(map(int, f.read().strip()))

size = len(data)
d = [1]*(size + 1)
for i, e in enumerate(data):
    d[e] = data[(i+2) % size - 1]

d1 = emulate(d[:], data[0], 100)

in_order = [d1[1]]
for _ in range(size - 2):
    in_order.append(d1[in_order[-1]])

print(''.join(map(str, in_order)))

d[data[-1]] = size + 1
size, iterations = 10**6, 10**7
d = d + list(range(len(d) + 1, size + 1)) + [data[0]]
d = emulate(d, data[0], iterations)
print(d[1] * d[d[1]])
