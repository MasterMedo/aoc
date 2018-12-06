from string import ascii_lowercase

def purge(s):
    i = 1
    while i < len(s):
        if abs(ord(s[i-1]) - ord(s[i])) == 32:
            del s[i-1:i+1]
            i = max(i-2, 0)
        i += 1
    return s

data = purge(list(open('../input/5.in').read().strip()))

print len(data)
print min(len(purge(filter(lambda x: x.lower() != c, data))) for c in ascii_lowercase)
