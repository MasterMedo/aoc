from itertools import pairwise

direction = {"U": -1j, "D": 1j, "L": -1, "R": 1}
sign = lambda x: x and (1, -1)[x < 0]

with open("../input/9.txt") as f:
    data = f.read().rstrip().split("\n")

rope = [0] * 10
part1 = set()
part2 = set()
for line in data:
    d, n = line.split()
    for _ in range(int(n)):
        rope[0] += direction[d]
        for H, T in pairwise(range(len(rope))):
            diff = rope[H] - rope[T]
            if abs(diff) >= 2:
                rope[T] += sign(diff.real) + sign(diff.imag) * 1j
        part1.add(rope[1])
        part2.add(rope[T])

print(len(part1))
print(len(part2))
