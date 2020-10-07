from hashlib import md5
from functools import lru_cache
from itertools import count
from collections import defaultdict

import sys

sys.setrecursionlimit(5000)


@lru_cache
def key(string, stretch=2016):
    hashed = md5(string.encode()).hexdigest()
    return hashed if not stretch else key(hashed, stretch - 1)


with open('../input/14.txt') as f:
    salt = f.read()[:-1]

keys = []
visited = set()
matches = defaultdict(list)

last_index = float('inf')
for index in count(1):
    if index > last_index:
        break

    first_triple = True
    current, count = None, 0
    for char in key(salt + str(index)):
        if current is None:
            current = char

        if current == char:
            count += 1

        else:
            current = char
            count = 1

        if first_triple and count == 3:
            first_triple = False
            matches[char].append(index)

        if count == 5:
            for match in matches[char]:
                if 1000 >= index - match > 0 and match not in visited:
                    visited.add(match)
                    keys.append(match)
                    if len(keys) == 64:
                        last_index = match + 1000

print(sorted(keys)[63])
