with open("../input/7.txt") as f:
    data = list(sorted(int(n) for n in f.read().split(",")))

median = data[len(data) // 2]
print(sum(abs(n - median) for n in data))

mean = sum(data) // len(data)
print(sum(abs(n - mean) * (abs(n - mean) + 1) // 2 for n in data))
