with open('../input/23.txt') as f:
    b = next(int(line[5:]) for line in f if line[:5] == 'set b')

print((b-2)**2)

counter = 0
b = b*100 + 100000
for i in range(b, b+17001, 17):
    for j in range(2, int(i**(1/2))):
        if i % j == 0:
            counter += 1
            break

print(counter)
