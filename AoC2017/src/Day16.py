with open ("../inputs/p16.txt") as f:
    data = f.read().split(',')

def solution(cap):
    p = list('abcdefghijklmnop')
    old = []
    for i in xrange(cap):
        if ''.join(p) in old:
            print(old[cap % i])
            return
        old.append(''.join(p))
        for ins in data:
            if ins[0] == 's':
                a = int(ins[1:])
                p = p[-a:] + p[:-a]
            elif ins[0] == 'x':
                a, b = map(int, ins[1:].split('/'))
                p[b], p[a] = p[a], p[b]
            elif ins[0] == 'p':
                a, b = map(int, map(p.index, ins[1:].split('/')))
                p[b], p[a] = p[a], p[b]
    print(''.join(p))

solution(1)
solution(1000000000)