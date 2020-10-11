from collections import defaultdict
from itertools import count


def to_int(x):
    return int(x) if x[-1].isdigit() else registers[x]


with open('../input/25.txt') as f:
    program = [[code, args] for code, *args in map(str.split, f)]

program_start = program[:]
for i in count(1):
    ip = 0
    program = program_start[:]
    registers = defaultdict(int)
    registers['a'] = i
    output = 0
    while ip < len(program):
        if output >= 50:
            print(i)
            exit(i)

        code, args = program[ip]
        x = args[0]
        if len(args) > 1:
            y = args[1]

        if code == 'cpy':
            registers[y] = to_int(x)

        elif code == 'inc':
            registers[x] += 1

        elif code == 'dec':
            registers[x] -= 1

        elif code == 'jnz':
            if to_int(x) != 0:
                ip += to_int(y)
                continue

        elif code == 'tgl':
            x = to_int(x) + ip
            if x >= len(program):
                continue

            elif program[x][0] == 'inc':
                program[x][0] = 'dec'

            elif len(program[x][1]) == 1:
                program[x][0] = 'inc'

            elif program[x][0] == 'jnz':
                program[x][0] = 'cpy'

            elif len(program[x][1]) == 2:
                program[x][0] = 'jnz'

        elif code == 'out':
            if to_int(x) != output % 2:
                break

            output += 1

        ip += 1
