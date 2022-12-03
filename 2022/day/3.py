from more_itertools import grouper


def score(char: str) -> int:
    if char.islower():
        return ord(char) - ord("a") + 1

    return ord(char) - ord("A") + 1 + 26


with open("../input/3.txt") as f:
    lines = f.read().strip().split("\n")

part1 = 0
for line in lines:
    left = line.strip()[: len(line) // 2]
    right = line.strip()[len(line) // 2 :]
    char = set(left).intersection(set(right)).pop()
    part1 += score(char)

part2 = 0
for line1, line2, line3 in grouper(lines, 3):
    char = set(line1).intersection(set(line2)).intersection(set(line3)).pop()
    part2 += score(char)

print(part1)
print(part2)
