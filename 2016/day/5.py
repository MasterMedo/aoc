import hashlib
import itertools

with open("../input/5.txt") as f:
    data = f.read().strip()

password = [-1 for i in range(8)]
for i in itertools.count():
    hex = hashlib.md5((data + str(i)).encode()).hexdigest()
    n = int(hex[5], 16)
    if hex[:5] == ('00000') and 0 <= n <= 7 and password[n] == -1:
            password[n] = hex[6]
            if -1 not in password:
                break

print ''.join(password)
