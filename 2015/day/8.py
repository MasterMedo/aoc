with open('../input/8.txt') as f:
    data = f.read().strip().splitlines()

print sum(len(i) - len(i.decode('unicode_escape')) + 2 for i in data)
print sum(len(i.encode('unicode_escape')) + 2 + i.count('\"') - len(i) for i in data)
