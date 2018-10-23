def digits(string):
    return [int(n) for n in string.split()]

with open("../input/02.txt") as f:
  rows = [digits(line) for line in f.read().strip().splitlines()]

print(sum(max(row)-min(row) for row in rows))
print(sum(a/b for row in rows for a in row for b in row if (a % b == 0 and a != b)))
