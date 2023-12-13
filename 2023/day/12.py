from functools import cache


@cache
def arrangements(springs, damaged_springs):
    if not damaged_springs:
        return 0 if springs.count("#") else 1

    window = damaged_springs[0]
    s = 0
    damaged = 0
    max_start = len(springs)
    for end, char in enumerate(springs):
        start = end - window + 1
        if start > max_start:
            break

        if char in "#?":
            damaged = min(damaged + 1, window)
            if char == "#" and max_start == len(springs):
                max_start = end
        else:
            damaged = 0

        next_char = "." if end + 1 == len(springs) else springs[end + 1]
        if damaged == window and next_char in ".?":
            s += arrangements(springs[end + 2:], damaged_springs[1:])

    return s


sum_arrangements = 0
sum_arrangements2 = 0
with open("../input/12.txt") as f:
    for line in f:
        springs, groups = line.split()
        damaged_springs = groups = tuple(map(int, groups.split(",")))
        sum_arrangements += arrangements(springs, damaged_springs)
        sum_arrangements2 += arrangements("?".join(springs for _ in range(5)), damaged_springs * 5)

print(sum_arrangements)
print(sum_arrangements2)
