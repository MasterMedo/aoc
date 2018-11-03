with open('../input/05.txt') as fp:
    data = map(int, fp.readlines())

pc = steps = 0
while pc < len(data):
    num = 1 # if data[pc] < 3 else -1
    data[pc] += num
    pc += data[pc] - num
    steps += 1
print steps



