first, last, seen = 0, 0, set()
r2 = 0
while True:
    r1 = r2 | 2**16
    r2 = 1250634
    while True:
        r2 = (((r2 + (r1 & 255)) & 16777215) * 65899) & 16777215
        if 256 > r1:
            break
        r1 = r1//256
    if not first:
        first = r2
    if r2 in seen:
        break
    seen.add(r2)
    last = r2

print(first)
print(last)

''' general solution, 0 sec part1, ~Xdays part 2 '''
# commands = {
#         'addr': lambda r, A, B: r[A] + r[B],
#         'addi': lambda r, A, B: r[A] + B,
#         'mulr': lambda r, A, B: r[A] * r[B],
#         'muli': lambda r, A, B: r[A] * B,
#         'banr': lambda r, A, B: r[A] & r[B],
#         'bani': lambda r, A, B: r[A] & B,
#         'borr': lambda r, A, B: r[A] | r[B],
#         'bori': lambda r, A, B: r[A] | B,
#         'setr': lambda r, A, B: r[A],
#         'seti': lambda r, A, B: A,
#         'gtir': lambda r, A, B: int(A > r[B]),
#         'gtri': lambda r, A, B: int(r[A] > B),
#         'gtrr': lambda r, A, B: int(r[A] > r[B]),
#         'eqir': lambda r, A, B: int(A == r[B]),
#         'eqri': lambda r, A, B: int(r[A] == B),
#         'eqrr': lambda r, A, B: int(r[A] == r[B]),
#         }

# with open('../input/21.txt') as f:
#     program, pc = [], int(next(f)[-2])
#     for opcode, A, B, C in map(str.split, f):
#         program.append(f"r[{C}] = commands['{opcode}'](r, {A}, {B})")
#         if opcode == 'eqrr':
#             n, i = len(program), int(A)

# seen, first, last = set(), 0, 0
# r = [0, 0, 0, 0, 0, 0]
# while r[pc] < len(program):
#     exec(program[r[pc]])
#     r[pc] += 1
#     if r[pc] == n:
#         if not first:
#             first = r[i]
#             print(first)
#         if r[i] in seen:
#             break
#         seen.add(r[i])
#         last = r[i]

# print(last)
