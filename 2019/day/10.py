from math import atan2, pi

with open('../input/10.txt') as f:
    asteroids = set((x, y) for y, l in enumerate(f)
                           for x, c in enumerate(l.strip()) if c == '#')

def angle(x, y, z, w):
    return 2*pi - atan2(z-x, w-y)

def dist(x, y, z, w):
    return abs(z-x) + abs(w-y)

n, xy = max((len(set(angle(*xy, *zw) for zw in asteroids if xy != zw)), xy)
                                     for xy in asteroids)

a = list(sorted(set(angle(*xy, *zw) for zw in asteroids)))[199]
x, y = min(filter(lambda zw: angle(*xy, *zw) == a and xy != zw, asteroids),
           key=lambda zw: dist(*xy, *zw))

print(n)
print(x*100 + y)
