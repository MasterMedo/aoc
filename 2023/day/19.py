import re
from math import prod
from collections import OrderedDict


def rate(part: dict[str, int], workflow: str) -> int:
    for rule in workflows[workflow].split(","):
        if ">" not in rule and "<" not in rule:
            next_workflow = rule
        else:
            sign = rule[1]
            category, bound, next_workflow = re.split(fr"{sign}|:", rule)
            if sign == ">":
                if part[category] <= int(bound):
                    continue
            else:
                if part[category] >= int(bound):
                    continue

        if next_workflow == "A":
            return sum(part.values())
        elif next_workflow == "R":
            return 0

        return rate(part, next_workflow)


with open("../input/19.txt") as f:
    workflows_raw, parts = map(str.splitlines, f.read().strip().split("\n\n"))

workflows = OrderedDict()
for workflow in workflows_raw:
    name, rules = workflow[:-1].split("{")
    workflows[name] = rules
workflow = "in"
rating = 0
for part in parts:
    part = eval("dict(" + part[1:-1] + ")")
    rating += rate(part, workflow)

print(rating)

to_visit = [({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}, "in")]
combinations = 0
while to_visit:
    part, workflow = to_visit.pop()
    if workflow == "A":
        combinations += prod(b - a + 1 for a, b in part.values())
        continue
    elif workflow == "R":
        continue

    for rule in workflows[workflow].split(","):
        if ">" not in rule and "<" not in rule:
            next_workflow = rule
        else:
            sign = rule[1]
            category, bound, next_workflow = re.split(fr"{sign}|:", rule)
            bound = int(bound)
            min_part, max_part = part[category]
            if sign == ">":
                if max_part <= bound:
                    continue
                elif min_part <= bound:
                    to_visit.append(({c: v if c != category else (bound + 1, max_part) for c, v in part.items()}, next_workflow))
                    max_part = bound
            else:
                if min_part >= bound:
                    continue
                elif max_part >= bound:
                    to_visit.append(({c: v if c != category else (min_part, bound - 1) for c, v in part.items()}, next_workflow))
                    min_part = bound
        part[category] = (min_part, max_part)
    to_visit.append((part, next_workflow))

print(combinations)
