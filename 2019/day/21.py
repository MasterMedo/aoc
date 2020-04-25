intcode = __import__('9').intcode

with open('../input/21.txt') as f:
    tape = list(map(int, f.read().split(',')))

part1 = """
OR A J
AND B J
AND C J
NOT J J
AND D J
WALK
""" # ~(ABC)D

part2 = """
OR A J
AND B J
AND C J
NOT J J
OR E T
OR H T
AND T J
AND D J
RUN
"""
springscript = (ord(c) for c in part2[1:])
for output in intcode(tape, springscript):
    if output <= 1114111:
        print(chr(output), end='')

print(output)
