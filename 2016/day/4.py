from collections import Counter
from itertools import groupby
from operator import itemgetter

with open('../input/4.txt') as f:
    data = [(''.join(line.split('-')[:-1]), line[:-2].split('-')[-1].split('[')) for line in f.readlines()]

print sum(int(i[1][0]) for i in data if set(i[1][1]) == set(''.join(''.join(sorted(*zip(*j[1])[:1])) for j in groupby(Counter(i[0]).most_common(), key=itemgetter(1)))[:5]))

for line in data:
    if 'north' in ''.join(chr((ord(i) - 97 + int(line[1][0])) % 26 + 97) for i in line[0]):
        print line[1][0]
