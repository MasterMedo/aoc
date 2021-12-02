with open("../input/1.txt") as f:
    depths = list(map(int, f.readlines()))

print(sum(depths[i - 1] < depths[i] for i in range(1, len(depths))))
print(sum(current > last for last, current in zip(depths, depths[3:])))
