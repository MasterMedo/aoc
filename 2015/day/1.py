with open('../input/1.txt') as f:
    data = [1 if i == '(' else -1 for i in f.read().strip()]

print sum(data)
print next(i for i in range(len(data)) if sum(data[:i]) == -1)
