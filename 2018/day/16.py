from re import findall

to_ints = lambda x: (map(int, findall('-?\d+', i)) for i in x.split('\n') if i)
with open('../input/16.txt') as f:
    test, program = map(to_ints, f.read().split('\n\n\n\n'))

commands = {
        'addr': lambda r, A, B: r[A] + r[B],
        'addi': lambda r, A, B: r[A] + B,
        'mulr': lambda r, A, B: r[A] * r[B],
        'muli': lambda r, A, B: r[A] * B,
        'banr': lambda r, A, B: r[A] & r[B],
        'bani': lambda r, A, B: r[A] & B,
        'borr': lambda r, A, B: r[A] | r[B],
        'bori': lambda r, A, B: r[A] | B,
        'setr': lambda r, A, B: r[A],
        'seti': lambda r, A, B: A,
        'gtir': lambda r, A, B: 1 if A > r[B] else 0,
        'gtri': lambda r, A, B: 1 if r[A] > B else 0,
        'gtrr': lambda r, A, B: 1 if r[A] > r[B] else 0,
        'eqir': lambda r, A, B: 1 if A == r[B] else 0,
        'eqri': lambda r, A, B: 1 if r[A] == B else 0,
        'eqrr': lambda r, A, B: 1 if r[A] == r[B] else 0,
        }

ambiguities = 0
translate = {}
for before, (number, A, B, C), after in zip(*[test]*3):
    potential = set()
    for opcode in commands:
        if commands[opcode](before, A, B) == after[C]:
            potential.add(opcode)

    if len(potential) >= 3:
        ambiguities += 1
        
    potential = potential.difference(set(translate.values()))
    if len(potential) == 1:
        translate[number] = potential.pop()

r = [0, 0, 0, 0]
for number, A, B, C in program:
    r[C] = commands[translate[number]](r, A, B)

print ambiguities
print r[0]
