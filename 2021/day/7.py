import math
from math import factorial as f
from functools import cache

@cache
def second_factorial(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n + 1) // f(2) // f(n -1)

with open('../input/7.txt') as fp:
    data = [int(n) for n in fp.read().split(',')]

part_1 = float('inf')
part_2 = float('inf')
for i in range(max(data)):
    part_1 = min(part_1, sum(abs(i - n) for n in data))
    part_2 = min(part_2, sum(second_factorial(abs(i - n)) for n in data))

print(part_1)
print(part_2)
