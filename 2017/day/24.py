def find(data, port):
    if not any(port in p for p in data):
        return 0, port

    s = lambda x, y: tuple(map(sum, zip(x, y)))
    return s((1, 2*port), max((find(data-{p}, p[port == p[0]])
        # for p in data if port in p), key=lambda x: x[1])) # part 1
        for p in data if port in p))) # part 2


with open('../input/24.txt') as f:
    data = set(tuple(map(int, line.split('/'))) for line in f)

print(find(data, 0)[1])
