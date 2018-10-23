def gen(data, part):
  while True:
    data[0] = data[0] * data[1] % data[2]
    if data[0] % (1 if part == 1 else data[3]) == 0:
      yield data[0] & 0xFFFF

with open("../input/15.txt") as f:
  tmp = [16807, 4, 48271, 8]
  data = {x.split()[1]: [int(x.split()[-1]), tmp.pop(0), 2147483647, tmp.pop(0)] for x in f.readlines()}

cnt = 0
A, B = gen(list(data['A']), 1), gen(list(data['B']), 1)
for i in xrange(40000000):
  if next(A) == next(B):
    cnt += 1

print cnt
cnt = 0
A, B = gen(list(data['A']), 2), gen(list(data['B']), 2)
for i in xrange(5000000):
  if next(A) == next(B):
    cnt += 1

print cnt
