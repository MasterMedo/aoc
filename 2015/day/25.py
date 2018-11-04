with open('../input/25.txt') as f:
    tmp = f.read().strip().replace(',', '').replace('.', '').split()
    x, y = int(tmp[-3]), int(tmp[-1])

num, t = 0, 1
a, b, c = 20151125, 252533, 33554393

while True:
    t += 1
    for i, j in zip(xrange(t - 1, 0, -1), xrange(1, t)):
        num += 1
        if i == x and y == j:
            for k in xrange(num - 1):
                a = a * b % c
            print a
            break


