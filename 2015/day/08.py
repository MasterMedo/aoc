with open('../input/08.txt') as fp:
    data = fp.read().strip().splitlines()

l, d, r = 0, 0, 0
for i in data:
    l += len(i)
    d += len(i.decode('unicode_escape')) - 2
    r += len(i.encode('unicode_escape')) + 2 + i.count('\"')

print l - d
print r - l
