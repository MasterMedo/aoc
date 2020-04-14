from itertools import permutations
from more_itertools import roundrobin
from collections import deque
intcode = __import__('9').intcode

with open('../input/7.txt') as f:
    tape = list(map(int, f.read().split(',')))

best = 0
# for permutation in permutations(range(5)): # uncomment for part1
for permutation in permutations(range(5, 10)): # comment for part1
    queue = list(map(lambda p: deque([p]), permutation))
    fromqueue = lambda i: (queue[i].popleft() for _ in iter(int, 1))
    amplifiers = [intcode(tape, fromqueue(i)) for i in range(5)]
    queue[0].append(0)
    for i, output in enumerate(roundrobin(*amplifiers)):
        queue[(i+1)%5].append(output)

    best = max(best, queue[0].pop())

print(best)
