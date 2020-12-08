def program(data):
    seen = set()
    acc = pc = 0
    while 0 <= pc < len(data) and pc not in seen:
        i, n = data[pc].split()
        seen.add(pc)
        if i == 'a':
            acc += int(n)
        elif i == 'j':
            pc += int(n)
            continue
        pc += 1

    return pc, acc


with open('../input/8.txt') as f:
    data = [line[0] + line[3:] for line in f]

print(program(data)[1])
for j in range(len(data)):
    if 'a' not in data[j]:
        data[j] = data[j].translate(str.maketrans('nj', 'jn'))
        pc, acc = program(data)
        data[j] = data[j].translate(str.maketrans('nj', 'jn'))
        if pc == len(data):
            print(acc)
            break
