def Solution(data, part1):
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
    if part1: part1 = False; print L[0]*L[1]; return

  hash = ""
  for i in range(16):
    tmp = 0
    for j in range(16):
      tmp ^= L[16*i+j]
    hash += format(tmp,'02x')
  print hash

with open("../input/10.txt") as f:
  fp = f.read()
  data1 = [int(i) for i in fp.replace(',',' ').split()]
  data2 = [ord(i) for i in list(fp)] + [17, 31, 73, 47, 23]

Solution(data2, Solution(data1, True))
