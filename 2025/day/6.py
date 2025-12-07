from math import prod


with open("../input/6.txt") as f:
    data = [line for line in f.readlines()]

col = 0
part1 = 0
part2 = 0
while col < len(data[-1]) - 1:
    prev = col
    col += 1
    while col < len(data[-1]) and data[-1][col] == " ":
        col += 1

    if data[-1][prev] == "+":
        part1 += sum(int(row[prev:col]) for row in data[:-1])
    else:
        part1 += prod(int(row[prev:col]) for row in data[:-1])

    arr = []
    for c in range(col - 1, prev - 1, -1):
        n = 0
        for row in data[:-1]:
            if row[c] not in [" ", "\n"]:
                n = n * 10 + int(row[c])
        if n != 0:
            arr.append(n)

    if data[-1][prev] == "+":
        part2 += sum(arr)
    else:
        part2 += prod(arr)


print(part1)
print(part2)
