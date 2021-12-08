from itertools import permutations

with open("../input/8.txt") as f:
    data = f.readlines()

d = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

part_1 = 0
part_2 = 0
for line in data:
    a, b = line.split(" | ")
    a = a.split()
    b = b.split()
    part_1 += sum(len(code) in {2, 3, 4, 7} for code in b)
    for permutation in permutations("abcdefg"):
        to = str.maketrans("abcdefg", "".join(permutation))
        a_ = ["".join(sorted(code.translate(to))) for code in a]
        b_ = ["".join(sorted(code.translate(to))) for code in b]
        if all(code in d for code in a_):
            part_2 += int("".join(str(d[code]) for code in b_))
            break

print(part_1)
print(part_2)
