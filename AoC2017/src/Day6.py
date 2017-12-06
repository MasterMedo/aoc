def digits(string):
    return [int(n) for n in string.split()]

with open("../inputs/Day6_input.txt") as f:
  rows = [digits(line) for line in f.read().strip().splitlines()]

# Part 1:
# block = rows[0]

# For part 2 insert the printed block from Part 1 as done here
block = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]
i = 0
blocks = []
while (sum(1 for b in blocks if b == block)!=1):
  z = []
  for o in block:
    z.append(o)
  blocks.append(z)
  i += 1
  j = 0
  tmp = max(block)
  while block[j] != tmp:
    j += 1
  block[j] = 0
  for k in range(tmp):
    j += 1
    if j > len(block)-1:
      j %= len(block)
    block[j] += 1
print block
print i