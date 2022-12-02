data = []
part1 = 0
part2 = 0
with open("../input/2.txt") as f:
    for line in f:
        a, b = line.split()
        a = int(a.translate(str.maketrans("ABC", "123")))
        b = int(b.translate(str.maketrans("XYZ", "123")))
        part1 += b
        if a == b:  # draw
            part1 += 3
        elif a == (b - 2) % 3 + 1:  # win
            part1 += 6
        if b == 1:  # lose
            part2 += (a - 2) % 3 + 1
        elif b == 2:  # draw
            part2 += a
            part2 += 3
        else:  # win
            part2 += a % 3 + 1
            part2 += 6

print(part1)
print(part2)
