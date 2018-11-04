import re

with open("../input/5.txt") as f:
    data = f.readlines()

print sum([1 for i in data if all(re.match(r, i) \
    for r in (".*([aeiou].*){3}", "^((?!ab|cd|xy|pq).)*$", ".*(.)\\1"))])
print sum([1 for i in data if re.match(".*((.)(.)).*\\1", i) and re.match(".*(.).\\1", i)])
