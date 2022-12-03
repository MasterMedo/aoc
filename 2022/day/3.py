from more_itertools import grouper


def score(char: str) -> int:
    if char.islower():
        return ord(char) - ord("a") + 1

    return ord(char) - ord("A") + 1 + 26


with open("../input/3.txt") as f:
    lines = f.read().strip().split("\n")

part1 = 0
for line in lines:
    mid = len(line) // 2
    char = set(line[:mid]) & set(line[mid:])
    part1 += score(char.pop())

part2 = 0
for group in grouper(lines, 3):
    part2 += score(set.intersection(*map(set, group)).pop())

print(part1)
print(part2)
