with open('../input/4.txt') as f:
    data = [(''.join(line.split('-')[:-1]), line[:-2].split('-')[-1].split('[')) for line in f.readlines()]

print sum(int(i[1][0]) for i in data if set(i[1][1]) == set(list(set(sorted(sorted(i[0]), key=i[0].count, reverse=True)))[:5]))

for line in data:
    if 'north' in ''.join(chr((ord(i) - 97 + int(line[1][0])) % 26 + 97) for i in line[0]):
        print line[1][0]
