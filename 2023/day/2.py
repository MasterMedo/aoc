import re

from collections import defaultdict

possible_games = 0
power = 0
with open("../input/2.txt") as f:
    for i, line in enumerate(f):
        cubes = defaultdict(int)
        subsets = line.strip().split(": ")[1].split("; ")
        for subset in subsets:
            for cube in subset.split(", "):
                amount, color = cube.split(" ")
                cubes[color] = max(cubes[color], int(amount))

        if cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14:
            possible_games += i + 1

        power += cubes["red"] * cubes["green"] * cubes["blue"]

print(possible_games)
print(power)
