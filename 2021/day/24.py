with open("../input/24.txt") as f:
    data = f.read().split("inp w\n")[1:]

z = []  # number in base 26
max_monad = [0] * 14
min_monad = [0] * 14
for i, chunk in enumerate(data):
    lines = chunk.split("\n")
    pop = int(lines[3][-2:]) == 26  # if digit should be popped from z
    x_add = int(lines[4].split()[-1])
    y_add = int(lines[14].split()[-1])

    if not pop:  # push digit to z
        z.append((i, y_add))
    else:  # apply restriction: last_z_digit == current_z_digit + difference
        j, y_add = z.pop()
        difference = x_add + y_add
        if difference < 0:
            max_monad[i] = 9 + difference
            max_monad[j] = 9
            min_monad[i] = 1
            min_monad[j] = 1 - difference
        elif difference > 0:
            max_monad[i] = 9
            max_monad[j] = 9 - difference
            min_monad[i] = 1 + difference
            min_monad[j] = 1
        else:
            max_monad[i] = max_monad[j] = 9
            min_monad[i] = min_monad[j] = 1

print("".join(map(str, max_monad)))
print("".join(map(str, min_monad)))
