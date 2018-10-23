def digits(string):
    return [int(n) for n in string.split('x')]

def sides(dim):
  return [dim[0]*dim[1], dim[0]*dim[2], dim[1]*dim[2]]

def sort(row):
  row.sort()
  return row

with open("../inputs/p02.txt") as f:
  rows = [digits(line) for line in f.read().strip().splitlines()]

print(sum(2*side for row in rows for side in sides(row)) + sum(min(sides(row)) for row in rows))
print(sum(2*(sort(row)[0]+sort(row)[1]) + row[0]*row[1]*row[2] for row in rows))
