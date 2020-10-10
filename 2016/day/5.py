from hashlib import md5
from itertools import count

with open("../input/5.txt") as f:
    data = f.read().strip()

part1 = []
part2 = [-1]*8
for i in count():
    code = md5((data + str(i)).encode()).hexdigest()
    n = int(code[5], 16)
    if code.startswith('00000'):
        if len(part1) < 8:
            part1.append(code[5])

        if 0 <= (n := int(code[5], 16)) <= 7 and part2[n] == -1:
            part2[n] = code[6]
            if -1 not in part2:
                break

print(''.join(part1))
print(''.join(part2))
