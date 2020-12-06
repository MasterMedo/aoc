with open('../input/6.txt') as f:
    data = f.read().strip().split('\n\n')

print(sum(len(set.union(*map(set, x.split('\n')))) for x in data))
print(sum(len(set.intersection(*map(set, x.split('\n')))) for x in data))
