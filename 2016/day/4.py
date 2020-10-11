import re


def common(soup):
    return set(sorted(set(soup), key=lambda c: (-soup.count(c), c))[:5])


def rot(soup, n):
    return ''.join(chr((ord(c) - 97 + int(n)) % 26 + 97) for c in soup)


with open('../input/4.txt') as f:
    data = [re.split(r'-|\[', line[:-2]) for line in f]

print(sum(int(n) for *abc, n, chk in data if set(chk) == common(''.join(abc))))
print(next(n for *abc, n, chk in data if 'north' in rot(''.join(abc), n)))
