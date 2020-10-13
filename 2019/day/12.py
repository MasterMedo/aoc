from math import gcd
from re import findall
from itertools import combinations, count


def lcm(x, y):
    return abs(x*y) // gcd(x, y)


with open('../input/12.txt') as f:
    moons = [[list(map(int, findall(r'-?\d+', line))), [0]*3] for line in f]

start = list(zip(*list(m for moon in moons for m in moon)))
energy = [[[0]*3, [0]*3] for _ in moons]
period = 1
for i in range(3):
    for t in count():
        for (s1, v1), (s2, v2) in combinations(moons, 2):
            v1[i] += (s1[i] < s2[i]) - (s1[i] > s2[i])
            v2[i] += (s2[i] < s1[i]) - (s2[i] > s1[i])

        for j, (s, v) in enumerate(moons):
            s[i] += v[i]
            if t == 999:
                energy[j][0][i] = abs(s[i])
                energy[j][1][i] = abs(v[i])

        if start[i] == list(zip(*list(m for moon in moons for m in moon)))[i]:
            period = lcm(period, t+1)
            break

print(sum(sum(moon[0]) * sum(moon[1]) for moon in energy))
print(period)
