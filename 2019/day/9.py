from collections import defaultdict

with open('../input/9.txt') as f:
    l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

i = 0
relative_base = 0
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
        l[state(i+1)] = int(input('input a number: '))
        i += 2

    elif optcode ==  4: # output
        print(f'output: {arg(i+1)}')
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
