from copy import deepcopy
from math import prod

starting_monkeys = []
with open("../input/11.txt") as f:
    for chunk in f.read().strip().split("\n\n"):
        _, items, operation, div, true, false = chunk.split("\n")
        items = list(map(int, items[18:].split(",")))
        operation = operation[13:].replace("new", "old").replace("old", "item")
        div = int(div[20:])
        true = int(true[28:])
        false = int(false[29:])
        starting_monkeys.append([items, operation, div, true, false])

product = prod(monkey[2] for monkey in starting_monkeys)

for iterations in (20, 10_000):
    monkeys = deepcopy(starting_monkeys)
    score = [0] * len(starting_monkeys)
    for _ in range(iterations):
        for i, (items, operation, div, true, false) in enumerate(monkeys):
            for item in items:
                score[i] += 1
                exec(operation)
                if iterations == 20:
                    item //= 3
                else:
                    item %= product
                monkeys[false if item % div else true][0].append(item)
            monkeys[i][0] = []

    print(prod(sorted(score)[-2:]))
