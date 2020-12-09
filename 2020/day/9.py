from collections import deque

with open('../input/9.txt') as f:
    data = list(map(int, f))

preamble = deque(data[:25])
for target in data[25:]:
    if all(target - i not in preamble for i in preamble):
        print(target)
        break

    preamble.popleft()
    preamble.append(target)

running_sum = 0
contiguous_set = deque()
for n in data:
    running_sum += n
    contiguous_set.append(n)
    while running_sum > target:
        running_sum -= contiguous_set.popleft()

    if running_sum == target and len(contiguous_set) > 1:
        print(min(contiguous_set) + max(contiguous_set))
        break
