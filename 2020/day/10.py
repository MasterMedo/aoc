with open('../input/10.txt') as f:
    data = sorted(map(int, f))

delta = {1: 0, 3: 1}
joltage = 0
for n in data:
    delta[n - joltage] += 1
    joltage = n

print(delta[1] * delta[3])

stairs = [1] + [0]*data[-1]
for n in data:
    stairs[n] = stairs[n-3] + stairs[n-2] + stairs[n-1]

print(stairs[-1])
