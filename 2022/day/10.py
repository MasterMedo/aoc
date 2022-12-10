x = 1
crt = [1]
with open("../input/10.txt") as f:
    for line in f:
        match line.split():
            case "addx", n:
                crt.append(x)
                x += int(n)
        crt.append(x)

print(sum(i * crt[i - 1] for i in [20, 60, 100, 140, 180, 220]))

i = 0
for _ in range(6):
    for x in range(40):
        if x in (crt[i] - 1, crt[i], crt[i] + 1):
            print("#", end="")
        else:
            print(" ", end="")
        i += 1
    print()
