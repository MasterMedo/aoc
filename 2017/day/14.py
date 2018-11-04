# Day 10
def bits(data):
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
      if num + i > length - 1: 
        for j in xrange(0, num + i - length): 
          L[j] = L[length + j]
      L = L[:length]
      i += (skip + num)
      skip += 1
      if i > length - 1: i %= length

  hash = ""
  for i in xrange(16):
    tmp = 0
    for j in xrange(16):
      tmp ^= L[16 * i + j]
    hash += format(tmp, '02x')
  s = ""
  for i in xrange(128 - len(bin(int(hash, 16))[2:])):
    s += '0'
  return s + bin(int(hash, 16))[2:]

# Day 14
def group(i, j, num):
  global grid
  grid[i][j][1] = num
  if i != 0   and grid[i - 1][j][0] == 1 and grid[i - 1][j][1] == 0: group(i - 1, j, num)
  if i != 127 and grid[i + 1][j][0] == 1 and grid[i + 1][j][1] == 0: group(i + 1, j, num)
  if j != 0   and grid[i][j - 1][0] == 1 and grid[i][j - 1][1] == 0: group(i, j - 1, num)
  if j != 127 and grid[i][j + 1][0] == 1 and grid[i][j + 1][1] == 0: group(i, j + 1, num)

with open("../input/14.txt") as f:
  data = f.read()

num = cnt = 0
grid = []
for row in range(128):
  binRow = bits([ord(i) for i in list(data + '-' + str(row))] + [17, 31, 73, 47, 23])
  for i in binRow: 
    if i == '1': cnt += 1
  grid.append([[int(x),0] for x in list(binRow)])
print cnt
for i in xrange(128):
  for j in xrange(128):
    if grid[i][j][0] == 1 and grid[i][j][1] == 0:
      num += 1
      group(i,j,num)

print num
