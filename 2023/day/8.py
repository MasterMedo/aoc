import re

from itertools import cycle
from math import lcm

with open("../input/8.txt") as f:
    instructions, lines = f.read().strip().split("\n\n")

commands = {}
for line in lines.split("\n"):
    start, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
    commands[start, "L"] = left
    commands[start, "R"] = right

node = "AAA"
for steps, instruction in enumerate(cycle(instructions)):
    node = commands[node, instruction]
    if node == "ZZZ":
        print(steps + 1)
        break

loop = []
for node, side in commands:
    if node.endswith("A") and side == "R":
        for steps, instruction in enumerate(cycle(instructions)):
            node = commands[node, instruction]
            if node.endswith("Z"):
                loop.append(steps + 1)
                break

print(lcm(*loop))
