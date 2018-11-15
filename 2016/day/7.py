import re
with open('../input/7.txt') as f:
    data = [(' '.join(j[::2]), ' '.join(j[1::2])) for j in (i[:-1].replace('[', ']').split(']') for i in f.readlines())]

print sum(1 for i in data if re.search(r'(\w)(?!\1)(\w)\2\1', i[0]) and not re.search(r'(\w)(?!\1)(\w)\2\1', i[1]))
print sum(1 for i in data if re.search(r'(\w)(?!\1)(\w)\1.*@.*\2\1\2', i[0] + '@' + i[1]))

