with open('../input/5.txt') as f:
    l = list(map(int, f.read().split(',')))

i = 0
jump = [None, 4, 4, 2, 2, 0, 0, 4, 4, 2]
while True:
    opcode, mode = l[i] % 100, str(l[i]//100).zfill(2)[::-1]
    arg = lambda x: l[l[i+x]] if mode[x-1] == '0' else l[i+x]

    if   opcode == 99: # halt
        break

    elif opcode ==  1: # add
        l[l[i+3]] = arg(1) + arg(2)

    elif opcode ==  2: # multiply
        l[l[i+3]] = arg(1) * arg(2)

    elif opcode ==  3: # input
        l[l[i+1]] = int(input('input a number: '))

    elif opcode ==  4: # output
        print(f'output: {arg(1)}')

    elif opcode ==  5: # jump if true
        i = arg(2) if arg(1) else i+3

    elif opcode ==  6: # jump if false
        i = arg(2) if not arg(1) else i+3

    elif opcode ==  7: # less than
        l[l[i+3]] = 1 if arg(1) < arg(2) else 0

    elif opcode ==  8: # equals
        l[l[i+3]] = 1 if arg(1) == arg(2) else 0

    else:              # error
        raise Exception(f'invalid opcode {opcode}')

    i += jump[opcode]
