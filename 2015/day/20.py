from math import *

with open('../input/20.txt') as f:
    data = int(f.read().strip())

for i in xrange(51, 2636363, 1):
    # if sum(filter(lambda x: i % x == 0, xrange(1, i + 1))) * 10 >= data:
    if sum(filter(lambda x: i % x == 0, xrange(i / 50, i + 1))) * 11 >= data:
        print i
        break
