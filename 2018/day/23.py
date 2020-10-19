import re

with open('../input/23.txt') as f:
    nanobots = [list(map(int, re.findall(r'-?\d+', line))) for line in f]

x, y, z, r = max(nanobots, key=lambda x: x[-1])
print(sum(abs(x-a) + abs(y-b) + abs(z-c) <= r
      for a, b, c, _ in nanobots))

from z3 import Int, If, Optimize

def Abs(x):
  return If(x >= 0, x, -x)

def Dist(x, y, z, a, b, c):
    return Abs(x-a) + Abs(y-b) + Abs(z-c)

X = x, y, z = Int('x'), Int('y'), Int('z')
cost = Int('cost')
constraint = x * 0
for *Y, r in nanobots:
  constraint += If(Dist(*X, *Y) <= r, 1, 0)

opt = Optimize()
opt.add(cost == constraint)
h1 = opt.maximize(cost)
h2 = opt.minimize(Dist(*(0, 0, 0), *X))
opt.check()
print(opt.lower(h2))
