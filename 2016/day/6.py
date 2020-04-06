with open('../input/6.txt') as f:
    columns = list(zip(*f.read().split('\n')[:-1]))

print(''.join(max(set(c), key = c.count) for c in columns))
print(''.join(min(set(c), key = c.count) for c in columns))
