with open('../input/1.txt') as f:
    data = map(int, list(f.read().strip()))

print sum(data[i] for i in range(len(data)) if data[i] == data[i - 1])
print sum(data[i] for i in range(len(data)) if data[i] == data[(i + len(data) / 2) % len(data)])
