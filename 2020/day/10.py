with open('../input/10.txt') as f:
    data = list(sorted(int(line) for line in f))

delta = [0]*4
joltage = 0
for n in data:
    delta[n-joltage] += 1
    joltage = n

print(delta[1] * delta[3])

stairs = [0]*(data[-1]+1)
stairs[0] = 1
for n in data:
    stairs[n] = stairs[n-3] + stairs[n-2] + stairs[n-1]

print(stairs[-1])
