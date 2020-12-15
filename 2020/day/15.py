with open('../input/15.txt') as f:
    data = list(map(int, f.read().split(',')))

seen = {last: i + 1 for i, last in enumerate(data)}
last = data[-1]

for turn in range(len(data) + 1, 30000000 + 1):
    current = turn - 1 - seen[last] if last in seen else 0
    seen[last] = turn - 1
    last = current
    if turn == 2020:
        print(current)

print(current)
