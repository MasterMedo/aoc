data = (i for i in open('../input/12.txt').read().split('\n') if i)
state = next(data)[15:]
rules = {i[0]: i[2] for i in map(str.split, data)}
psum = lambda s, off: sum(i-off*4 for i, c in enumerate(s) if c == '#')

it = 1000
for i in xrange(it):
    state = '....' + state + '....'
    old = state
    state = '..' + ''.join(rules[state[j-2:j+3]] for j in range(2, len(state) - 3))
    if i == 19:
        print psum(state, 20)

print psum(state, it) + (50000000000 - it) * (psum(state, it) - psum(old, it))
