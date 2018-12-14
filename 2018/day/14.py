n = open('../input/14.txt').read().strip()
x, y = 0, 1
l = [3, 7]

while n not in ''.join(map(str, l[-7:])):
    s = l[x] + l[y]
    l.extend(list(map(int, str(s))))
    x = (x+l[x]+1) % len(l)
    y = (y+l[y]+1) % len(l)

print ''.join(map(str, l[int(n):int(n) + 10]))
print ''.join(map(str, l)).index(n)
