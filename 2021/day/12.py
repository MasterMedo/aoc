from collections import defaultdict


def dfs(start, seen, part_2=False):
    if start == "end":
        return 1

    s = 0
    for end in d[start]:
        if end not in seen:
            tmp = {end} if end == end.lower() else set()
            s += dfs(end, seen | tmp, part_2)
        elif part_2 and end != "start":
            s += dfs(end, seen, False)

    return s


with open("../input/12.txt") as f:
    data = f.readlines()

d = defaultdict(set)
for line in data:
    start, end = line.strip().split("-")
    d[start].add(end)
    d[end].add(start)

print(dfs("start", {"start"}))
print(dfs("start", {"start"}, True))
