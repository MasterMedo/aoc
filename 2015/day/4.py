import hashlib
import itertools

with open("../input/4.txt") as f:
    data = f.read().strip()

for i in itertools.count():
    hex = hashlib.md5((data + str(i)).encode()).hexdigest()
    if hex.startswith('000000'): # '00000'
        print(i)
        break
