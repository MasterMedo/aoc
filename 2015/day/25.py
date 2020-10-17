with open('../input/25.txt') as f:
    row, column = [int(n[:-1]) for n in f.read().split() if n[0].isdigit()]

code = (column + row - 1) * (column + row) // 2 - row
print(20151125 * pow(252533, code, 33554393) % 33554393)
