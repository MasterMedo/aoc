from collections import defaultdict


def bfs(start, seen, part_2=False):
    if start == "end":
        return 1

    s = 0
    for end in d[start]:
        if end not in seen:
            tmp = {end} if end == end.lower() else set()
            s += bfs(end, seen | tmp, part_2)
        elif part_2 is None and end != "start":
            s += bfs(end, seen, end)

    return s


d = defaultdict(set)
with open("../input/12.txt") as f:
    data = f.readlines()

for line in data:
    start, end = line.strip().split("-")
    d[start].add(end)
    d[end].add(start)

print(bfs("start", {"start"}))
print(bfs("start", {"start"}, None))
