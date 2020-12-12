with open('../input/12.txt') as f:  # file
    data = [(cmd, int(''.join(n))) for cmd, *n in f]

d = 1
xy = 0
for cmd, n in data:
    if cmd == 'F':
        xy += d*n
    elif cmd == 'L':
        d *= 1j**(n//90)
    elif cmd == 'R':
        d /= 1j**(n//90)
    elif cmd == 'N':
        xy += n*1j
    elif cmd == 'S':
        xy -= n*1j
    elif cmd == 'E':
        xy += n
    elif cmd == 'W':
        xy -= n

print(int(abs(xy.real) + abs(xy.imag)))

xy = 0
w = 10 + 1j
for cmd, n in data:
    if cmd == 'F':
        xy += n*w
    elif cmd == 'L':
        w *= 1j**(n//90)
    elif cmd == 'R':
        w /= 1j**(n//90)
    elif cmd == 'N':
        w += n*1j
    elif cmd == 'S':
        w -= n*1j
    elif cmd == 'E':
        w += n
    elif cmd == 'W':
        w -= n

print(int(abs(xy.real) + abs(xy.imag)))
