from collections import Counter

data = open('../input/2.txt').read().strip().splitlines()
counts = [set(Counter(i).values()) for i in data]

print sum(1 for i in counts if 2 in i) * sum(1 for i in counts if 3 in i)
print next(key for i in range(len(data[0])) for key, val in Counter(k[:i] + k[i+1:] for k in data).iteritems() if val == 2)
