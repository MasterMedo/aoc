from math import *

def score(l):
    myHp, myAtt, myDef = [sum(i) for i in zip(*l)]
    myHp = 100
    return True if ceil(bHp / (myAtt - bDef if myAtt - bDef > 0 else 1)) <= \
            ceil(myHp / (bAtt - myDef if bAtt - myDef > 0 else 1)) else False

with open('../input/21.txt') as fp, open('../input/21-shop.txt') as fs:
    shop = [[map(int, j.split()[1:]) for j in i.splitlines()[1:]] for i in fs.read().strip().split("\n\n")]
    bHp, bAtt, bDef = [int(i.split(': ')[1]) for i in fp.read().strip().splitlines()]

shop[1].append((0, 0, 0))
shop[2].extend([(0, 0, 0), (0, 0, 0)])
print min(sum(i[0] for i in [w, a, r1, r2]) for w in shop[0] for a in shop[1] for r1 in shop[2] for r2 in shop[2] if score([w, a, r1, r2]) and r1 != r2)
print max(sum(i[0] for i in [w, a, r1, r2]) for w in shop[0] for a in shop[1] for r1 in shop[2] for r2 in shop[2] if not score([w, a, r1, r2]) and r1 != r2)
