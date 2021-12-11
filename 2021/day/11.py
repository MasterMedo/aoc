data = {}
with open("../input/11.txt") as f:
    for y, row in enumerate(f.readlines()):
        for x, n in enumerate(row.strip()):
            data[(x, y)] = int(n)

border = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
step = 0
total_flashes = 0
while True:
    step += 1
    for key in data:
        data[key] += 1

    stack = [key for key in data if data[key] == 10]
    while stack:
        x, y = stack.pop()
        for dx, dy in border:
            x_ = x + dx
            y_ = y + dy
            if (x_, y_) in data and data[x_, y_] < 10:
                data[x_, y_] += 1
                if data[x_, y_] == 10:
                    stack.append((x_, y_))

    flashes = 0
    for key in data:
        if data[key] == 10:
            data[key] = 0
            flashes += 1

    total_flashes += flashes
    if step == 100:
        print(total_flashes)

    if flashes == 100:
        print(step)
        break
