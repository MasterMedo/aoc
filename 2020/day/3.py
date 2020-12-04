from itertools import count

with open('../input/3.txt') as f:
    data = [line.strip() for line in f]

product = 1
for x, y in [(1, 1), (5, 1), (7, 1), (1, 2), (3, 1)]:
    trees = 0
    for row, col in zip(range(0, len(data), y), count(0, x)):
        if data[row][col % len(data[0])] == '#':
            trees += 1

    product *= trees

print(trees)
print(product)
