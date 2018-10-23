with open("../input/18.txt") as f:
    data = [x.strip().split() for x in f.readlines()]

def num(a):
    try:
        return int(a)
    except ValueError:
        global regs
        if a not in regs:
            regs[a] = 0
        return regs[a]

regs = {}
j = 0
while True:
    i = data[j]
    if i[0] == 'snd':
        snd = num(i[1])
    elif i[0] == 'set':
        regs[i[1]] = num(i[2])
    elif i[0] == 'add':
        regs[i[1]] = num(i[1]) + num(i[2])
    elif i[0] == 'mul':
        regs[i[1]] = num(i[1]) * num(i[2])
    elif i[0] == 'mod':
        regs[i[1]] = num(i[1]) % num(i[2])
    elif i[0] == 'rcv':
        if num(i[1]) > 0:
            print snd
            break
    elif i[0] == 'jgz':
        if num(i[1]) > 0:
            j = j + num(i[2]) - 1
    j += 1
