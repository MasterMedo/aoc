from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/15.txt') as f:
    tape = list(map(int, f.read().split(',')))

i = None
xy = 0
reverse = [2, 1, 4, 3]
moves = list(range(1, 5))
directions = [1j, -1j, -1, 1]
grid = defaultdict(lambda: 3)
robot = intcode(tape, (i := moves.pop() for _ in iter(int, 1)))

for block in robot:
    zw = xy + directions[i-1]
    if block:
        xy = zw
        if grid[xy] == 4:
            moves.append(reverse[i-1])

        for j, d in enumerate(directions):
            if grid[xy+d] == 3:
                moves.append(j+1)
                grid[xy+d] = 4

    grid[zw] = block
    if not moves:
        break

# for y in range(21, -20, -1):
#     print(''.join('#.$ ?'[grid[x+y*1j]] if x+y*1j != xy else 'D'
#                   for x in range(-21, 22)))

xy = 0
# xy = next(xy for xy in grid if grid[xy] == 2)  # uncomment for part2
visit = [xy]
distance = defaultdict(int)
while visit:
    xy = visit.pop()
    if grid[xy] == 2 and distance[xy] > 2:
        break

    for d in directions:
        if grid[xy+d] and not distance[xy+d]:
            visit.append(xy+d)
            distance[xy+d] = distance[xy] + 1

print(max(distance.values()))
