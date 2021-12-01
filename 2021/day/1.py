with open("../input/1.txt") as f:
    depths = list(map(int, f.readlines()))

print(sum(depths[i - 1] < depths[i] for i in range(1, len(depths))))
print(
    sum(
        sum(depths[i - 3 : i]) < sum(depths[i - 2 : i + 1])
        for i in range(3, len(depths))
    )
)
