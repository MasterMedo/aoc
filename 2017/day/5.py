with open('../input/5.txt') as f:
    data = map(int, f.readlines())

pc = steps = 0
while pc < len(data):
    num = 1 # if data[pc] < 3 else -1
    data[pc] += num
    pc += data[pc] - num
    steps += 1
print steps



