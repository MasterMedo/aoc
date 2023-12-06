from math import prod


def ways(time, distance):
    for delta in range(time):
        if (time - delta) * delta > distance:
            break
    return time - 2*delta + 1


with open("../input/6.txt") as f:
    times, distances = (line.split()[1:] for line in f.readlines())

print(prod(ways(int(t), int(d)) for t, d in zip(times, distances)))
print(ways(int("".join(times)), int("".join(distances))))
