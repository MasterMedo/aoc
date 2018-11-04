import random

def swap(s, sub, repl):
    find = s.find(sub)
    while find != -1:
        yield s[:find] + repl + s[find + len(sub):]
        find = s.find(sub, find + 1)

with open('../input/19.txt') as fp:
    tmp = [i.split(' => ') for i in fp.read().splitlines() if i != '']
    molecule = tmp.pop()[0]
    replacements = {y: i for x, y in tmp for i, j in tmp if j == y}

print(len(set([j for i in replacements for j in swap(molecule, replacements[i], i)])))

for i in xrange(10): # increase if needed
    cnt, mole = 0, molecule
    for z in xrange(10000): 
        i = random.choice(list(replacements))
        find = mole.find(i)
        if find != -1:
            cnt += 1
            mole = mole[:find] + replacements[i] + mole[find + len(i):]
            if mole == 'e':
                print(cnt)
                break
