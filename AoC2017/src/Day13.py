def severity(x,y):
  return x*y if x%(y*2-2) == 0 else 0

with open("../inputs/p13.txt") as f:
  data = [[int(x), int(y)] for x,y in [line.strip().split(': ') for line in f.readlines()]]

print sum(severity(x,y) for x,y in data)

i = 0
while True:
  part2 = True
  for x,y in data:
    if i+y != 0:
      if (x+i)%(y*2-2) == 0:
        part2 = False
        break
  if part2:
    print i
    break
  i += 1
