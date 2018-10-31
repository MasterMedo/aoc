from math import *

with open('../input/20.txt') as fp:
    data = int(fp.read().strip())

for i in range(51, 2636363, 1):
    # if sum(filter(lambda x: i % x == 0, range(1, i + 1))) * 10 >= data:
    if sum(filter(lambda x: i % x == 0, range(i / 50, i + 1))) * 11 >= data:
        print i
        break
