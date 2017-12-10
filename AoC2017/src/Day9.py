def group(mine):
  global i
  total = 0
  while i < len(data):
    if data[i] == '<': i += 1; garbage()
    elif data[i] == '{': i += 1; total += group(mine+1)
    elif data[i] == '}': return total + mine
    i += 1
  return total + mine

def garbage():
  global i, garb
  while data[i] != ">":
    garb += 1
    if data[i] == "!":
      i += 1
      garb -= 1
    i += 1

with open("../inputs/Day9_input.txt") as f:
  data = list(f.read().replace('\n',''))

i = garb = 0
print group(0)
print garb