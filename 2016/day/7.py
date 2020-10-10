import re

palindrom = re.compile(r'(\w)(?!\1)(\w)\2\1')
aba_bab = re.compile(r'(\w)(?!\1)(\w)\1.*@.*\2\1\2')

TLS = SSL = 0
with open('../input/7.txt') as f:
    for line in f:
        segments = re.split(r'\[|\]', line[:-1])
        outside = ' '.join(segments[::2])
        inside = ' '.join(segments[1::2])
        if re.search(palindrom, outside) and not re.search(palindrom, inside):
            TLS += 1

        if re.search(aba_bab, inside + '@' + outside):
            SSL += 1

print(TLS)
print(SSL)
