with open('../input/4.txt') as f:
    x, y = map(int, f.read().split('-'))

c = 0
for i in range(x, y+1):
    f = False
    s = str(i)
    d = 0
    for j in range(len(s)-1):
        if s[j] > s[j+1]:
            break
        if s[j] == s[j+1]:
            d += 1
        else:
            if d == 1:
                f = True
            d = 0
    else:
        if f or d == 1:
            c += 1

print(c)
