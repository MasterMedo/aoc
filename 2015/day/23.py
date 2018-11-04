f = {
        'hlf': lambda r, pc, x: (r / 2, pc + 1),
        'tpl': lambda r, pc, x: (r * 3, pc + 1),
        'inc': lambda r, pc, x: (r + 1, pc + 1),
        'jmp': lambda r, pc, x: (r, pc + int(x)),
        'jie': lambda r, pc, x: (r, pc + int(x) if r % 2 == 0 else pc + 1),
        'jio': lambda r, pc, x: (r, pc + int(x) if r == 1 else pc + 1)
    }

with open('../input/23.txt') as fp:
    instructions = [i.split() for i in fp.read().strip().replace('+', '').replace(',', '').splitlines()]

# pc, r = 0, {'a': 0, 'b': 0}
pc, r = 0, {'a': 1, 'b': 0}
while True:
    if pc >= len(instructions):
        print r['b']
        break
    cur = instructions[pc]
    register = cur[1] if cur[1] in r else 'a'
    r[register], pc = f[cur[0]](r[register], pc, cur[-1])
