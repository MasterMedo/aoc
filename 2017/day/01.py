with open('../input/01.txt') as fp:
    data = map(int, list(fp.read().strip()))

print sum(data[i] for i in range(len(data)) if data[i] == data[i - 1])
print sum(data[i] for i in range(len(data)) if data[i] == data[(i + len(data)/2) % len(data)])
