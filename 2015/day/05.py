import re

with open("../input/05.txt") as f:
    input = f.read().strip().splitlines()

print sum([1 for i in input if all(re.match(r, i) \
    for r in (".*([aeiou].*){3}", "^((?!ab|cd|xy|pq).)*$", ".*(.)\\1"))])
print sum([1 for i in input if re.match(".*((.)(.)).*\\1", i) and re.match(".*(.).\\1", i)])
