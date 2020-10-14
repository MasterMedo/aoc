from itertools import accumulate

with open('../input/16.txt') as f:
    sequence_ = sequence = f.read()[:-1]

offset = int(sequence[:7])

base_pattern = [0, 1, 0, -1]
sequence = list(map(int, sequence))
for phase in range(100):
    new_sequence = [0] * len(sequence)
    for i in range(len(sequence)):
        pattern = (element for _ in iter(int, None)
                   for element in base_pattern for _ in range(i + 1))
        next(pattern)
        new_sequence[i] = abs(sum(j*k for j, k in zip(sequence, pattern))) % 10
    sequence = new_sequence

print(*sequence[:8], sep='')

sequence = list(map(int, sequence_*10000))[offset:][::-1]

for _ in range(100):
    sequence = list(accumulate(sequence, lambda x, y: (x + y) % 10))

print(*sequence[::-1][:8], sep='')
