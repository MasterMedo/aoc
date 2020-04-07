alphabet = 'abcdefghijklmnopqrstuvwxyz'[::-1]

with open('../input/11.txt') as f:
    passwd = list(f.read()[-2::-1])

i, n = 0, 2
while n:
    if passwd[i] == 'z':
        passwd[i] = 'a'
        i += 1
        continue

    passwd[i] = chr(ord(passwd[i])+1)
    i = 0

    test = ''.join(passwd)
    if any(alphabet[i:i+3] in test for i in range(24)) \
            and all(c not in test for c in 'iol') \
            and sum(c*2 in test for c in alphabet) > 1:
        n -= 1
        print(test[::-1])
