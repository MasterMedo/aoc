# part2 initially done by hand, here is one neat solution inspired by /u/akho_
from math import sqrt

def nex(x, y):
    if x ==  y == 0:       return 1, 0
    if x >  -y and x >  y: return x, y + 1
    if x >  -y and x <= y: return x - 1, y
    if x <= -y and x <  y: return x, y - 1
    if x <= -y and x >= y: return x + 1, y

with open('../input/3.txt') as f:
    data = int(f.read().strip())

x = int(sqrt(data)) + 1
print (x - 1) / 2 - (data - (x * x - x + 1)) + x / 2

x = y = 0
m = {(0, 0): 1}
while m[(x, y)] <= data:
    x, y = nex(x, y)
    m[(x, y)] = sum(m.get((x + i, y + j), 0) for i in [-1, 0, 1] for j in [0, 1, -1])
print m[(x, y)]
