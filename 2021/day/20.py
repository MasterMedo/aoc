from itertools import count


with open("../input/20.txt") as f:
    tape, image = f.read()[:-1].split("\n\n")

lights = set()
for y, row in enumerate(image.split("\n")):
    for x, pixel in enumerate(row):
        if pixel == "#":
            lights.add((x, y))

for step in count(1):
    lights_ = set()
    minx = min(x for x, y in lights)
    maxx = max(x for x, y in lights)
    miny = min(y for x, y in lights)
    maxy = max(y for x, y in lights)
    for y in range(miny - 2, maxy + 2):
        for x in range(minx - 2, maxx + 2):
            binary = 0
            for b in range(3):
                for a in range(3):
                    if (x + a, y + b) in lights:
                        binary += pow(2, (2 - b) * 3 + (2 - a))
                    elif tape[0] == "#" and step % 2 == 0:
                        if (x + a) < minx or (x + a) > maxx:
                            binary += pow(2, (2 - b) * 3 + (2 - a))
                        elif (y + b) < miny or (y + b) > maxy:
                            binary += pow(2, (2 - b) * 3 + (2 - a))

            if tape[binary] == "#":
                lights_.add((x + 1, y + 1))

    lights = lights_
    if step == 2:
        print(len(lights))

    if step == 50:
        print(len(lights))
        break
