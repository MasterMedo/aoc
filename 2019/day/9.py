from collections import defaultdict

def intcode(l, inp):
    i = r = 0
    jump = [None, 4, 4, 2, 2, 0, 0, 4, 4, 2]
    while True:
        opcode, mode = l[i] % 100, str(l[i]//100).zfill(3)[::-1]
        arg = lambda x: l[pos(x)]
        def pos(x):
            d = {'0': l[x+i], '1': x+i, '2': r + l[x+i]}
            return d[mode[x-1]]

        if   opcode == 99: # halt
            break

        elif opcode ==  1: # add
            l[pos(3)] = arg(1) + arg(2)

        elif opcode ==  2: # multiply
            l[pos(3)] = arg(1) * arg(2)

        elif opcode ==  3: # input
            l[pos(1)] = next(inp)

        elif opcode ==  4: # output
            yield arg(1)

        elif opcode ==  5: # jump if true
            i = arg(2) if arg(1) else i+3

        elif opcode ==  6: # jump if false
            i = arg(2) if not arg(1) else i+3

        elif opcode ==  7: # less than
            l[pos(3)] = 1 if arg(1) < arg(2) else 0

        elif opcode ==  8: # equals
            l[pos(3)] = 1 if arg(1) == arg(2) else 0

        elif opcode ==  9: # relative_base
            r += arg(1)

        else:              # error
            raise Exception(f'invalid opcode {opcode}')

        i += jump[opcode]

if __name__ == '__main__':
    with open('../input/9.txt') as f:
        l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

    for o in intcode(l, (int(input('input: ')) for _ in iter(int, 1))):
        print(f'output: {o}')
