with open('../input/6.txt') as f:
    data = zip(*f.readlines())[:-1]

print ''.join(max(set(lst), key = lst.count) for lst in data)
print ''.join(min(set(lst), key = lst.count) for lst in data)
