with open('../input/3.txt') as f:
    data = [line.strip() for line in f]

rows = len(data)
cols = len(data[0])
forest = []
for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    col = row = trees = 0
    while row < rows:
        row = row % rows
        col = col % cols
        if data[row][col] == '#':
            trees += 1

        col += x
        row += y
    forest.append(trees)

for t in forest[1:]:
    forest[0] *= t

print(forest[1])
print(forest[0])
