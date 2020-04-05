from collections import defaultdict
from functools import partial
from blessed import Terminal

term = Terminal()
echo = partial(print, end = '', flush = True)

with open('../input/13.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

i = r = x = y = z = 0
grid = defaultdict(int)
l[0] = 2 # comment for part one
with term.cbreak():
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
            echo(term.home)
            for y in range(50, 0, -1):
                line = []
                for x in range(50):
                    line.append(' ' if grid[x, y] == 0 else grid[x, y])
                echo(''.join(str(o) for o in line)+'\n')
            char = term.inkey()
            code = 0 if char == 'k' else -1 if char == 'h' else 1
            l[state(i+1)] = code
            i += 2

        elif optcode ==  4: # output
            if z % 3 == 0:
                x = arg(i+1)
            elif z % 3 == 1:
                y = arg(i+1)
            elif arg(i+1) > 4:
                score = arg(i+1)
            else:
                grid[x, y] = arg(i+1)

            i += 2
            z += 1

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

        else: # error
            print(f'error: {optcode}')
            exit()


# print(sum(grid[k] == 2 for k in grid)) # uncomment for part 1
print(score)
