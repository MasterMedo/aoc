with open('../input/1.txt', 'r') as f:
    data = [int(line) for line in f]

for i, x in enumerate(data):
    for j, y in enumerate(data[i:], 1):
        if x + y == 2020:
            part1 = x * y
        for k, z in enumerate(data[i+j:]):
            if x + y + z == 2020:
                part2 = x * y * z

print(part1)
print(part2)
