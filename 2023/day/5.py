from itertools import batched


def solve(from_ranges, maps):
    for m in maps:
        from_ranges.sort()
        to_ranges = []
        for conversion in m.split("\n")[1:]:
            to_value, from_value, length = map(int, conversion.split())
            difference = to_value - from_value
            a, b = from_value, from_value + length - 1
            new_from_ranges = []
            for x, y in from_ranges:
                if a <= y and x <= b:
                    if a >= x and b <= y:  # x a b y
                        to_ranges.append((a + difference, b + difference))
                        if a > x:
                            new_from_ranges.append((x, a - 1))
                        if b < y:
                            new_from_ranges.append((b + 1, y))
                    elif a >= x:  # x a y b
                        to_ranges.append((a + difference, y + difference))
                        if a > x:
                            new_from_ranges.append((x, a - 1))
                    elif b <= y:  # a x b y
                        to_ranges.append((x + difference, b + difference))
                        if b < y:
                            new_from_ranges.append((b + 1, y))
                    else:  # a x y b
                        to_ranges.append((x + difference, y + difference))
                else:
                    new_from_ranges.append((x, y))
            from_ranges = new_from_ranges
        for equal in from_ranges:
            to_ranges.append(equal)
        from_ranges = to_ranges
    return next(iter(sorted(to_ranges)))[0]


with open("../input/5.txt") as f:
    seeds, *maps = f.read().strip().split("\n\n")

seeds = list(map(int, seeds.split()[1:]))
from_ranges = [(value, value + length) for value, length in batched(seeds, 2)]

print(solve([(seed, seed + 1) for seed in seeds], maps))
print(solve(from_ranges, maps))
