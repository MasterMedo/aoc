from itertools import count

with open("../input/25.txt") as f:
    d = {(x, y): c for y, line in enumerate(f.read().strip().split("\n")) for x, c in enumerate(line)}

X = max(x for x, y in d) + 1
Y = max(y for x, y in d) + 1
for step in count(1):
    flag = False
    d_ = d.copy()
    for x, y in d:
        x_ = (x + 1) % X
        y_ = y
        if d[x, y] == '>' and d[x_, y_] == '.':
            d_[x, y] = '.'
            d_[x_, y_] = '>'
            flag = True

    d = d_
    d_ = d.copy()
    for x, y in d:
        x_ = x
        y_ = (y + 1) % Y
        if d[x, y] == 'v' and d[x_, y_] == '.':
            d_[x, y] = '.'
            d_[x_, y_] = 'v'
            flag = True
    d = d_
    if not flag:
        print(step)
        break
