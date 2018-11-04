with open("../input/13.txt") as f:
    data = [map(int, i[:-1].split(': ')) for i in f.readlines()]

print sum(x * y if x % (y * 2 - 2) == 0 else 0 for x, y in data)

i = 0
while True:
  part2 = True
  for x, y in data:
    if i + y != 0 and (x + i) % (y * 2 - 2) == 0:
        part2 = False
        break
  if part2:
    print i
    break
  i += 1
