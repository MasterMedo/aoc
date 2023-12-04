import re

from collections import defaultdict

sum1 = 0
cards = defaultdict(int)
with open("../input/4.txt") as f:
    for i, line in enumerate(f):
        _, win, got = re.split(":|\|", line)
        win = set(win.strip().split())
        p = sum(n in win for n in got.strip().split())
        if p:
            sum1 += pow(2, p - 1)
            for j in range(p):
                cards[i + 1 + j + 1] += cards[i + 1] + 1

print(sum1)
print(sum(cards.values()) + i + 1)
