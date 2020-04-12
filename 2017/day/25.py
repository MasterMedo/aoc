from collections import defaultdict

states = {}
with open('../input/25.txt') as f:
    data = f.read().split('\n\n')
    state = data[0][15]
    steps = int(next(w for w in data[0].split() if w.isdigit()))
    for block in data[1:]:
        l = block.split('\n')
        states[l[0][-2]] = ((int(l[2][-2]), l[3][27], l[4][-2]),
                            (int(l[6][-2]), l[7][27], l[8][-2]))

tape = defaultdict(bool)
x = 0
for _ in range(steps):
    value, direction, state = states[state][tape[x]]
    tape[x] = value
    x += 1 if direction == 'r' else -1

print(sum(tape.values()))
