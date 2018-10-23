import hashlib
import itertools

with open("../input/04.txt") as f:
    input = f.read().strip()

for i in itertools.count():
    hex=hashlib.md5((input+str(i)).encode()).hexdigest()
    # for first part only 5 zeros '00000'
    if hex.startswith('000000'):
        print(i)
        break
