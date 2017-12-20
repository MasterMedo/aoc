with open("../inputs/p09.txt") as f:
  data = list(f.read().replace('\n',''))

i = lvl = depth = garbage = 0
ExFlag = GaFlag = False
while i < len(data):
  if data[i] == '{' and not GaFlag: depth += 1
  elif data[i] == '}' and not GaFlag: lvl += depth; depth -= 1
  elif data[i] == '<' and not GaFlag: GaFlag = True
  elif data[i] == '>' and GaFlag: GaFlag = False
  elif data[i] == '!' and GaFlag: i += 1
  elif GaFlag: garbage += 1
  i += 1

print lvl
print garbage