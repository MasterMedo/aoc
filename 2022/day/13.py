from itertools import zip_longest
from functools import cmp_to_key
from copy import deepcopy


def first(left, right, i, j):
    if isinstance(left[j], int) and isinstance(right[j], list):
        left[j] = [left[j]]
    if isinstance(right[j], int) and isinstance(left[j], list):
        right[j] = [right[j]]
    if isinstance(left[j], int) and isinstance(right[j], int):
        if left[j] < right[j]:
            score.append(i)
            return True, -1
        if left[j] > right[j]:
            return True, 1
        return False, 0
    k = 0
    while True:
        if k >= len(right[j]) and k >= len(left[j]):
            return False, 0
        if k >= len(right[j]):
            return True, 1
        if k >= len(left[j]):
            score.append(i)
            return True, -1
        x, y = first(left[j], right[j], i, k)
        if x:
            return True, y
        else:
            k += 1
    print("error")


def cmp(left, right):
    left = deepcopy(left)
    right = deepcopy(right)
    j = 0
    while True:
        if j >= len(right):
            return 1
        if j >= len(left):
            score.append(i)
            return -1
        x, y = first(left, right, i, j)
        if x:
            return y
        else:
            j += 1


with open("../input/13.txt") as f:
    pairs = f.read().rstrip().split("\n\n")

score = []
packets = []
part1 = 0
for i, pair in enumerate(pairs, 1):
    left, right = map(eval, pair.split("\n"))
    if cmp(left, right) == -1:
        part1 += i
    packets.append(left)
    packets.append(right)

packets.append([[6]])
packets.append([[2]])
part2 = 1
packets = list(sorted(packets, key=cmp_to_key(cmp)))
for i, packet in enumerate(packets, 1):
    if packet == [[6]] or packet == [[2]]:
        part2 *= i

print(part1)
print(part2)
