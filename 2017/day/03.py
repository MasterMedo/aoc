# Part 1
# Sadly, it only works on inputs on the left side of the spiral
input = 325489
a = 1
b = 0
c = 3
while a < input:
  a = c*c
  b += 1
  c += 2
c -= 2
print "Solution to part1:", (c-1)/2 - (input - (a-c+1)) + b

# Part 2
# Not my solution (a really bad one as well - this was for no whitespace golfing)
input = 325489
a = [-1,0,1]
r = (1,) * 99
x = y = s = n = 0
d = [[0 for g in r] for h in r]
d[0][0] = u = 1
while 1:
  if s == 0:
    n += 1
    s = 2 * n
    u =- u
  s -= 1
  o = s//n * u
  x += o
  y += u - o
  i = d[x][y] = sum([d[x+j][y+k] for j in a for k in a])
  if i > input:
    print "Solution to part 2:", i
    break