with open('../input/01.txt') as fp:
    data = [1 if i == "(" else -1 for i in fp.read().strip()]

print sum(data)
print min([i for i in range(len(data)) if sum(data[:i]) == -1])
