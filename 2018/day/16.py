from re import findall

ops = {
        'addr': lambda r, A, B: r[A] + r[B],
        'addi': lambda r, A, B: r[A] + B,
        'mulr': lambda r, A, B: r[A] * r[B],
        'muli': lambda r, A, B: r[A] * B,
        'banr': lambda r, A, B: r[A] & r[B],
        'bani': lambda r, A, B: r[A] & B,
        'borr': lambda r, A, B: r[A] | r[B],
        'bori': lambda r, A, B: r[A] | B,
        'setr': lambda r, A, _: r[A],
        'seti': lambda r, A, _: A,
        'gtir': lambda r, A, B: int(A > r[B]),
        'gtri': lambda r, A, B: int(r[A] > B),
        'gtrr': lambda r, A, B: int(r[A] > r[B]),
        'eqir': lambda r, A, B: int(A == r[B]),
        'eqri': lambda r, A, B: int(r[A] == B),
        'eqrr': lambda r, A, B: int(r[A] == r[B]),
        }

to_ints = lambda x: (map(int, findall('-?\d+', i)) for i in x.split('\n') if i)
with open('../input/16.txt') as f:
    test, program = map(to_ints, f.read().split('\n\n\n\n'))

count, trans = 0, {}
for before, (n, A, B, C), after in zip(*[test]*3):
    cand = set(code for code in ops if ops[code](before, A, B) == after[C])
    if len(cand) >= 3:
        count += 1
    cand = cand - set(trans.values())
    if len(cand) == 1:
        trans[n] = cand.pop()

r = [0] * 4
for n, A, B, C in program:
    r[C] = ops[trans[n]](r, A, B)

print count
print r[0]
