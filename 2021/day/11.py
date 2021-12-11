from itertools import count

data = {}
with open("../input/11.txt") as f:
    for y, row in enumerate(f.readlines()):
        for x, n in enumerate(row.strip()):
            data[(x, y)] = int(n)

height = y + 1
width = x + 1
flashes = 0
for step in count(1):
    stack = []
    seen = set()
    for key in data:
        data[key] += 1
        if data[key] > 9:
            stack.append(key)
            seen.add(key)

    while stack:
        x, y = stack.pop()
        for dx, dy in [
            ( 1, -1), ( 1, 0), ( 1, 1),
            ( 0, -1),          ( 0, 1),
            (-1, -1), (-1, 0), (-1, 1),
        ]:
            x_ = x + dx
            y_ = y + dy
            if 0 <= x_ < width and 0 <= y_ < height:
                data[x_, y_] += 1
                if (x_, y_) not in seen:
                    if data[x_, y_] > 9:
                        seen.add((x_, y_))
                        stack.append((x_, y_))

    flashes += len(seen)
    for x, y in seen:
        data[x, y] = 0

    if step == 100:
        print(flashes)

    if len(seen) == height * width:
        print(step)
        break
