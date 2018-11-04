with open("../input/2.txt") as f:
  rows = [map(int, i.split()) for i in f.readlines()]

print(sum(max(row) - min(row) for row in rows))
print(sum(a / b for row in rows for a in row for b in row if (a % b == 0 and a != b)))
