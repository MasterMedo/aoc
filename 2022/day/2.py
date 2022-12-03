part1 = 0
part2 = 0
with open("../input/2.txt") as f:
    for line in f:
        a, b = line.split()
        a = int(a.translate(str.maketrans("ABC", "123")))
        b = int(b.translate(str.maketrans("XYZ", "123")))
        part1 += b + ((b - a + 1) % 3) * 3
        part2 += (a + b) % 3 + 1 + (b - 1) * 3

print(part1)
print(part2)
