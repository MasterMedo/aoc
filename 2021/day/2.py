forward = 0
depth_1 = 0
depth_2 = 0
aim = 0

with open("../input/2.txt") as f:
    for line in f:
        direction, n = line.split()
        n = int(n)
        if direction == "forward":
            forward += n
            depth_2 += aim * n
        elif direction == "up":
            depth_1 -= n
            aim -= n
        elif direction == "down":
            aim += n
            depth_1 += n

print(forward * depth_1)
print(forward * depth_2)
