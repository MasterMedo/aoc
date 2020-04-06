with open('../input/20.txt') as f:
    path = f.read()[1:-2]

way = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
depth, stack = {0: 0}, []
xy = zw = 0
for c in path:
    if c in 'NEWS':
        xy += way[c]
        if xy not in depth or depth[xy] > depth[zw]+1:
            depth[xy] = depth[zw]+1
    elif c == '(':
        stack.append(xy)
    elif c == ')':
        xy = stack.pop()
    elif c == '|':
        xy = stack[-1]
    zw = xy

print(max(depth.values()))
print(len([x for x in depth.values() if x >= 1000]))
