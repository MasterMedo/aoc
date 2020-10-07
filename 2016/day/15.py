import re
from itertools import count


with open('../input/15.txt') as f:
    discs = [list(map(int, re.findall(r'[0-9]+', line[:-1])))
             for line in f]

# discs.append([len(discs) + 1, 11, 0, 0])  # uncomment for part2

print(next(time for time in count()
           if all((time + position + start) % mod == 0
                  for position, mod, _, start in discs)))
