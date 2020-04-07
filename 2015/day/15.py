import re
from math import prod

with open('../input/15.txt') as f:
    data = [list(map(int, re.findall(r'-?\d+', line))) for line in f]

max_score, best_cookie_score = 0, 0
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l = 100-i-j-k
            score = prod(max(0, sum(y*z for y,z in zip(x, (i,j,k,l))))
                    for x in list(zip(*data))[:-1])

            calories = sum(x[-1]*y for x, y in zip(data, (i,j,k,l)))
            max_score = max(max_score, score)
            if calories == 500:
                best_cookie_score = max(best_cookie_score, score)

print(max_score)
print(best_cookie_score)
