with open('../input/25.txt') as f:
    row, column = [int(n[:-1]) for n in f.read().split() if n[0].isdigit()]

code = ((row + column)**2 - 3*row-column)//2
print(pow(252533, code, 33554393)*20151125 % 33554393)
