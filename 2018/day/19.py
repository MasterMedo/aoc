goal = 2 ** 2 * 19 * 11 + 2 * 22 + 20
print sum(i for i in range(1, goal + 1) if goal % i == 0)
goal += (27 * 28 + 29) * 30 * 14 * 32
print sum(i for i in range(1, goal + 1) if goal % i == 0)


''' brute force elf code, ~30sec part1, ~XXXdays part2 '''

#with open('../input/19.txt') as f:
#    pc, *rest, program = *f.readlines(), []
#    pc = int(pc.split()[-1])
#    for opcode, A, B, C in map(str.split, rest):
#        program.append('r['+C+'] = commands[\''+opcode+'\'](r, '+A+', '+B+')')
#
#commands = {
#        'addr': lambda r, A, B: r[A] + r[B],
#        'addi': lambda r, A, B: r[A] + B,
#        'mulr': lambda r, A, B: r[A] * r[B],
#        'muli': lambda r, A, B: r[A] * B,
#        'banr': lambda r, A, B: r[A] & r[B],
#        'bani': lambda r, A, B: r[A] & B,
#        'borr': lambda r, A, B: r[A] | r[B],
#        'bori': lambda r, A, B: r[A] | B,
#        'setr': lambda r, A, B: r[A],
#        'seti': lambda r, A, B: A,
#        'gtir': lambda r, A, B: int(A > r[B]),
#        'gtri': lambda r, A, B: int(r[A] > B),
#        'gtrr': lambda r, A, B: int(r[A] > r[B]),
#        'eqir': lambda r, A, B: int(A == r[B]),
#        'eqri': lambda r, A, B: int(r[A] == B),
#        'eqrr': lambda r, A, B: int(r[A] == r[B]),
#        }
#
#r = [0, 0, 0, 0, 0, 0]
#r[0] = 1 # comment for part1
#while r[pc] < len(program):
#    exec(program[r[pc]])
#    r[pc] += 1


''' brute force python, 1sec part1, ~XXdays part2 '''

#r0 = r1 = r2 = r3 = r4 = r5 = 0
#r0 = 1 # comment for part1
#
#r1 = (r1 + 2)**2 * 19 * 11 + r2
#r2 = (r2 + 2) * 22 + 20
#r1 += (27*28+29)*30*14*32 # comment for part1
#r5 = 1
#while True:
#    r4 = 1
#    while True:
#        if r4 * r5 == r1:
#            r0 += r5
#        r4 += 1
#        if r4 > r1:
#            r5 += 1
#            if r5 > r1:
#                print r0
#                exit()
#            break
