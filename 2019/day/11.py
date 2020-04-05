from collections import defaultdict

with open('../input/11.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

i = 0
relative_base = 0
xy, robot_instructions, direction = 0j, 0, 1j
neighbour = {(1j,0):-1, (1j,1):1, (1,0):1j, (1,1):-1j,
             (-1j,0):1, (-1j,1):-1, (-1,0):-1j, (-1,1):1j}

grid = defaultdict(int, {0: 1}) # part 1: 1 -> 0
while True:
    optcode = l[i] % 100
    mode = list(reversed(list(map(int, str(l[i]//100)))))
    def state(x):
        if x-i-1 >= len(mode) or mode[x-i-1] == 0:
            return l[x]
        elif mode[x-i-1] == 1:
            return x
        elif mode[x-i-1] == 2:
            return relative_base + l[x]

    arg = lambda x: l[state(x)]

    if   optcode == 99: # halt
        break

    elif optcode ==  1: # add
        l[state(i+3)] = arg(i+1) + arg(i+2)
        i += 4

    elif optcode ==  2: # multiply
        l[state(i+3)] = arg(i+1) * arg(i+2)
        i += 4

    elif optcode ==  3: # input
        l[state(i+1)] = grid[xy]
        i += 2

    elif optcode ==  4: # output
        if robot_instructions % 2 == 0:
            grid[xy] = arg(i+1)
        else:
            direction = neighbour[direction, arg(i+1)]
            xy += direction

        robot_instructions += 1
        i += 2

    elif optcode ==  5: # jump if true
        if arg(i+1):
            i = arg(i+2)
        else:
            i += 3

    elif optcode ==  6: # jump if false
        if arg(i+1) == 0:
            i = arg(i+2)
        else:
            i += 3

    elif optcode ==  7: # less than
        l[state(i+3)] = 1 if arg(i+1) < arg(i+2) else 0
        i += 4

    elif optcode ==  8: # equals
        l[state(i+3)] = 1 if arg(i+1) == arg(i+2) else 0
        i += 4

    elif optcode == 9: # relative_base
        relative_base += arg(i+1)
        i += 2

    else: # error
        print(f'error: {optcode}')
        exit()

print(len(grid))
for y in range(-100, 100):
    for x in range(-100, 100):
        print('#' if grid[x+y*1j] else ' ', end='')
    print()
