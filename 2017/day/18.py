from time import sleep
from collections import deque

def run(instructions, p=0):
    i, reg = 0, {'p': p}
    while True:
        code, *args = instructions[i]
        num = lambda x: int(x) if x[-1].isdigit() else reg.get(x, 0)
        arg = lambda x: num(args[x-1])
        if   code == 'snd': queue[p].append(sound := arg(1))
        elif code == 'set': reg[args[0]] = arg(2)
        elif code == 'add': reg[args[0]] = arg(1) + arg(2)
        elif code == 'mul': reg[args[0]] = arg(1) * arg(2)
        elif code == 'mod': reg[args[0]] = arg(1) % arg(2)
        elif code == 'rcv': reg[args[0]] = yield
        elif code == 'jgz': i += arg(2)-1 if arg(1) > 0 else 0
        i += 1

with open("../input/18.txt") as f:
    data = list(map(str.split, f))

counter = 0
queue = [deque([]), deque([])]
next(program0 := run(data, 0))
next(program1 := run(data, 1))
print(queue[0][-1])

while queue[0] or queue[1]:
    if queue[0]:
        program1.send(queue[0].popleft())
    if queue[1]:
        counter += 1
        program0.send(queue[1].popleft())

print(counter)
