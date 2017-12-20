def Solution(data):
  LEN = 256
  L = [i for i in range(LEN)]
  i = skip = 0
  for k in range(64):
    for num in data:
      for j in range(LEN): L.append(L[j])
      tmp = []
      for j in L: tmp.append(j)
      for j in range(i,num+i): L[j] = tmp[num+2*i-j-1]
      if num+i > LEN-1: 
        for j in range(0, num+i-LEN): 
          L[j] = L[LEN+j]
      L = L[:LEN]
      i += (skip+num)
      skip += 1
      if i > LEN-1: i %= LEN

  hash = ""
  for i in range(16):
    tmp = 0
    for j in range(16):
      tmp ^= L[16*i+j]
    hash += format(tmp,'02x')
  s = ""
  for i in xrange(128 - len(bin(int(hash, 16))[2:])):
    s += '0'
  return s + bin(int(hash, 16))[2:]

with open("../inputs/p14.txt") as f:
  data = f.read()

cnt = 0
for row in range(128):
  tmp = data + '-' + str(row)
  data2 = [ord(i) for i in list(tmp)] + [17, 31, 73, 47, 23]
  binRow = Solution(data2)
  for i in binRow:
    if i == '1': cnt += 1
print cnt