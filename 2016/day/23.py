from math import factorial as f

with open('../input/23.txt') as fp:
    program = list(map(str.split, fp))

print(f(7) + int(program[19][1])*int(program[20][1]))
print(f(12) + int(program[19][1])*int(program[20][1]))
