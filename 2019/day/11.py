from collections import defaultdict

with open('../input/11.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

i = r = z = 0
xy, direction = 0j, 1j
neighbour = {(1j,0):-1, (1j,1):1, (1,0):1j, (1,1):-1j,
             (-1j,0):1, (-1j,1):-1, (-1,0):-1j, (-1,1):1j}

grid = defaultdict(int, {0: 1}) # comment for part 1
# grid = defaultdict(int)         # uncomment for part 1
while True:
    optcode = l[i] % 100
    mode = list(reversed(list(map(int, str(l[i]//100)))))
    arg = lambda x: l[state(x)]
    def state(x):
        if x-i-1 >= len(mode) or mode[x-i-1] == 0:
            return l[x]
        elif mode[x-i-1] == 1:
            return x
        elif mode[x-i-1] == 2:
            return r + l[x]

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
        if z % 2 == 0:
            grid[xy] = arg(i+1)
        else:
            direction = neighbour[direction, arg(i+1)]
            xy += direction
        z += 1
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

    elif optcode ==  9: # relative_base
        r += arg(i+1)
        i += 2

    else:               # error
        print(f'error: {optcode}')
        exit()


print(len(grid))
for y in range(0, -6, -1):
    for x in range(0, 40):
        print('#' if grid[x+y*1j] else ' ', end='')
    print()
