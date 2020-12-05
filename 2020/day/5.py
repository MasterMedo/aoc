with open('../input/5.txt') as f:
    ids = list(sorted(int(''.join('01'[c in 'BR'] for c in line), base=2)
                      for line in f.read().splitlines()))

print(ids[-1])
print(next(e+1 for i, e in enumerate(ids) if e+1 != ids[i+1]))
