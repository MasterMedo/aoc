def expansion(present: set[int], increase: int) -> list[int]:
    expansions = []
    empty = 0
    for i in range(max(present) + 1):
        if i not in present:
            empty += increase
        expansions.append(empty)
    return expansions


def distance(galaxies: list[int], increase: int) -> int:
    r_expansion = expansion(rows, increase)
    c_expansion = expansion(cols, increase)

    distance = 0
    for r1, c1 in galaxies:
        for r2, c2 in galaxies:
            distance += abs(r2 + r_expansion[r2] - r1 - r_expansion[r1]) + abs(c2 + c_expansion[c2] - c1 - c_expansion[c1])
    return distance // 2


galaxies = []
with open("../input/11.txt") as f:
    rows = set()
    cols = set()
    for r, row in enumerate(f.read().strip().split("\n")):
        for c, char in enumerate(row):
            if char == "#":
                galaxies.append((r, c))
                rows.add(r)
                cols.add(c)

print(distance(galaxies, 1))
print(distance(galaxies, 1_000_000 - 1))
