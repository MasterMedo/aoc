with open("../input/3.txt") as f:
    data = [list(line.strip()) for line in f]

epsilon = ''
gamma = ''

for bits in zip(*data):
    zeros = bits.count('0')
    ones = len(data) - zeros
    epsilon += '01'[ones > zeros]
    gamma += '10'[ones > zeros]

print(int(epsilon, 2) * int(gamma, 2))

codes = data[:]
for i in range(len(data[0])):
    zeros = sum(code[i] == '0' for code in codes)
    ones = len(codes) - zeros
    common_bit = '01'[ones >= zeros]
    codes = [code for code in codes if code[i] == common_bit]
    if len(codes) == 1:
        oxygen = ''.join(codes[0])
        break

codes = data[:]
for i in range(len(data[0])):
    zeros = sum(code[i] == '0' for code in codes)
    ones = len(codes) - zeros
    common_bit = '01'[ones < zeros]
    codes = [code for code in codes if code[i] == common_bit]
    if len(codes) == 1:
        carbon = ''.join(codes[0])
        break

print(int(oxygen, 2) * int(carbon, 2))
