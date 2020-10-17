import re

with open('../input/5.txt') as f:
    data = f.readlines()

rules = r'([aeiou].*){3}', r'(.)\1', r'^((?!ab|cd|pq|xy).)*$'
# rules = r'(..).*\1', r'(.).\1'
print(sum(all(re.search(pattern, i) for pattern in rules) for i in data))
