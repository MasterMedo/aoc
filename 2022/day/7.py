from collections import defaultdict
from itertools import accumulate


sizes = defaultdict(int)
stack = []
with open("../input/7.txt") as f:
    for line in f:
        if line.startswith("$ ls") or line.startswith("dir"):
            continue

        match line.split():
            case "$", "cd", "..":
                stack.pop()
            case "$", "cd", directory:
                stack.append(directory)
            case size, _:
                for path in accumulate(stack, func=lambda a, b: a + "/" + b):
                    sizes[path] += int(size)

print(sum(size for size in sizes.values() if size <= 100_000))
print(min(size for size in sizes.values() if size >= sizes["/"] - 40_000_000))
