def isValid(passwd):
    global abc
    passwd = ''.join(passwd)
    return  sum([1 for i in range(2, 26) if abc[i-2:i+1] in passwd]) > 0\
            and not set(passwd).intersection({'i','o','l'})\
            and sum([1 for i in abc if i+i in passwd]) > 1

def inc(passwd, n):
    global abc
    if n < -7:
        return passwd
    try:
        passwd[n] = abc[abc.index(passwd[n]) + 1]
    except Exception:
        passwd[n] = abc[0]
        passwd = inc(passwd, n-1)
    return passwd

def next(passwd):
    passwd = inc(passwd, -1)
    while not isValid(passwd):
        passwd = inc(passwd, -1)
    return passwd

abc = 'abcdefghijklmnopqrstuvwxyz'

with open('../input/11.txt') as fp:
    data = list(fp.read().strip())

first = next(data)
print ''.join(first)
print ''.join(next(first))
