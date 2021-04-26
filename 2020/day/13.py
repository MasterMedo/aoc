from math import prod
from sympy.ntheory.modular import crt

with open('../input/13.txt') as f:
    time = int(next(f))
    busses = [(int(bus), -i)
              for i, bus in enumerate(next(f).split(',')) if bus != 'x']

print(prod(min((-time % bus, bus) for bus, _ in busses)))
print(crt(*zip(*busses))[0])
