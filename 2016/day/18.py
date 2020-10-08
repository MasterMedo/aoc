with open('../input/18.txt') as f:
    row = {i: c == '^' for i, c in enumerate(f.read()[:-1])}

row_length = len(row)
safe = row_length - sum(row.values())
row[-1] = row[row_length] = False

for i in range(40 - 1):  # replace 40 with 400000 for part 2
    new_row = {}
    for x in range(row_length):
        trap = row[x-1] and not row[x+1] or not row[x-1] and row[x+1]
        new_row[x] = trap
        safe += not trap

    row = new_row
    row[-1] = row[row_length] = False

print(safe)
