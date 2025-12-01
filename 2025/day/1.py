with open("../input/1.txt") as f:
    lines = [(2 * (line[0] == "R") - 1, int(line[1:])) for line in f.readlines()]

part1 = 0
part2 = 0
dial = 50
for sign, amount in lines:
    div, mod = divmod(dial + sign * amount, 100)
    part1 += mod == 0
    part2 += abs(div) - (dial == 0 and sign == -1) + (mod == 0 and sign == -1)
    dial = mod

print(part1)
print(part2)
