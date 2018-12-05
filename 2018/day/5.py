from string import ascii_lowercase

def purge(s):
    a = 0
    while a < len(s)-1:
        if abs(ord(s[a]) - ord(s[a+1])) == 32:
            del s[a:a+2]
            a -= 2
        a += 1
    return s

data = purge(list(open('../input/5.txt').read().strip()))

print len(data)
print min(len(purge(filter(lambda x: x.lower() != c, data))) for c in ascii_lowercase)
