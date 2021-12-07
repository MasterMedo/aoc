with open("../input/7.txt") as fp:
    data = [int(n) for n in fp.read().split(",")]

part_1 = float("inf")
part_2 = float("inf")
for i in range(max(data)):
    part_1 = min(part_1, sum(abs(i - n) for n in data))
    part_2 = min(part_2, sum(abs(i - n) * (abs(i - n) + 1) // 2 for n in data))

print(part_1)
print(part_2)
