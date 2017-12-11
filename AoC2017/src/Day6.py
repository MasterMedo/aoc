def digits(string):
    return [int(n) for n in string.split()]

def solution(block):
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
  print i
  return block

with open("../inputs/p06.txt") as f:
  rows = [digits(line) for line in f.read().strip().splitlines()]

solution(solution(rows[0]))