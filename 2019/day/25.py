from collections import defaultdict
intcode = __import__('9').intcode

with open('../input/25.txt') as f:
    code = defaultdict(int, dict(enumerate(map(int, f.read().split(',')))))

game_input = (ord(c) for _ in iter(int, 1) for c in (input()+'\n'))
for c in map(chr, intcode(code, game_input)):
    print(c, end='')
