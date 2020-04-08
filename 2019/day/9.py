from collections import defaultdict

def intcode(tape, int_input):
    i = rb = 0
    jump  = [4, 4, 2, 2, 0, 0, 4, 4, 2]
    modes = lambda x, m: [tape[x+i], x+i, rb+tape[x+i]][m]
    while True:
        opcode = tape[i] % 100
        mode = str(tape[i]//100).zfill(3)[::-1]
        arg = lambda x: tape[pos(x)]
        pos = lambda x: modes(x, int(mode[x-1]))

        if   opcode == 99: break
        elif opcode ==  1: tape[pos(3)] = arg(1) + arg(2)
        elif opcode ==  2: tape[pos(3)] = arg(1) * arg(2)
        elif opcode ==  3: tape[pos(1)] = next(int_input)
        elif opcode ==  4: yield arg(1)
        elif opcode ==  5: i = arg(2) if arg(1) else i+3
        elif opcode ==  6: i = arg(2) if not arg(1) else i+3
        elif opcode ==  7: tape[pos(3)] = arg(1) < arg(2)
        elif opcode ==  8: tape[pos(3)] = arg(1) == arg(2)
        elif opcode ==  9: rb += arg(1)
        else: raise Exception(f'invalid opcode {opcode}')

        i += jump[opcode-1]

if __name__ == '__main__':
    with open('../input/9.txt') as f:
        l = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

    for o in intcode(l, (int(input('input: ')) for _ in iter(int, 1))):
        print(f'output: {o}')
