def solve(data, part1):
  length = 256
  L = range(length)
  i = skip = 0
  for k in xrange(64):
    for num in data:
      for j in xrange(length):
          L.append(L[j])
      tmp = []
      for j in L:
          tmp.append(j)
      for j in xrange(i, num + i):
          L[j] = tmp[num + 2 * i - j - 1]
      if num+i > length - 1: 
        for j in xrange(0, num + i - length): 
          L[j] = L[length + j]
      L = L[:length]
      i += skip + num
      skip += 1
      if i > length - 1:
          i %= length
    if part1:
        part1 = False
        print L[0] * L[1]
        return
  hash = ""
  for i in xrange(16):
    tmp = 0
    for j in xrange(16):
      tmp ^= L[16 * i + j]
    hash += format(tmp, '02x')
  print hash

with open("../input/10.txt") as f:
  tmp = f.read().strip()
  data1 = [int(i) for i in tmp.split(',')]
  data2 = [ord(i) for i in list(tmp)] + [17, 31, 73, 47, 23]

solve(data2, solve(data1, True))
