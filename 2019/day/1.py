with open('../input/1.txt') as f:
    data = list(map(int, f.read().split('\n')[:-1]))

fuel = lambda x: fuel(x//3-2) + x if x > 0 else 0
print(sum(x//3-2 for x in data))
print(sum(fuel(x//3-2) for x in data))
