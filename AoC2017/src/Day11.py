with open("../inputs/p11.txt") as f:
  data = [i for i in f.read().replace(',',' ').split()]

x = y = z = sol = 0
for card in data:
  if card == 'n': y += 1; z -= 1
  elif card == 's': y -= 1; z += 1
  elif card == 'ne': x += 1; z -= 1
  elif card == 'sw': x -= 1; z += 1
  elif card == 'nw': x -= 1; y += 1
  elif card == 'se': x += 1; y -= 1 
  dist = (abs(x) + abs(y) + abs(z)) / 2:
  sol = dist if sol < dist else sol

print (abs(x) + abs(y) + abs(z)) / 2
print sol
