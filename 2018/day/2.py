from collections import Counter
from operator import mul
from itertools import chain

data = open('../input/2.txt').read().strip().splitlines()

print reduce(mul, Counter(chain(*[set(Counter(i).values()).intersection(set([2, 3])) for i in data])).values())
print next(key for i in range(len(data[0])) for key, val in Counter(k[:i] + k[i+1:] for k in data).iteritems() if val == 2)
