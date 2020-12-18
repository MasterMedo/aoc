import re


class Int(int):
    def __mul__(self, o):
        return Int(int(o) + self)

    def __add__(self, o):
        return Int(int(o) + self)

    def __sub__(self, o):
        return Int(int(o) * self)


s1 = s2 = 0
with open('../input/18.txt') as f:
    for line in f.read().splitlines():
        line = line.replace('*', '-')
        s1 += eval(re.sub(r'(\d+)', r'Int(\1)', line))
        s2 += eval(re.sub(r'(\d+)', r'Int(\1)', line.replace('+', '*')))

print(s1)
print(s2)
