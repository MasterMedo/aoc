import re
from math import sqrt, ceil

with open("../input/17.txt") as f:
    xmin, xmax, ymin, ymax = map(int, re.findall(r"[-\d]+", f.read()))

# assumes ymin, ymax are negative
print(abs(ymin) * abs(ymin + 1) // 2)

velocities = 0
for dx_init in range(min(0, xmin - 1), max(0, xmax + 1)):
    for dy_init in range(ymin, abs(ymin)):
        solved = False
        dx = dx_init
        dy = dy_init
        x = 0
        y = 0
        while y > ymin:
            x += dx
            y += dy
            if dx < 0:
                dx += 1
            if dx > 0:
                dx -= 1
            dy -= 1
            if xmin <= x <= xmax and ymin <= y <= ymax:
                velocities += 1
                break

print(velocities)
