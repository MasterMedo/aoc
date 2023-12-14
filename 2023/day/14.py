def tilt(
    rocks_set: frozenset[tuple[complex, str]],
    d: complex,
) -> frozenset[tuple[complex, str]]:
    rocks = {rc: char for rc, char in rocks_set}
    for rc in sorted(rocks, key=lambda z: z.real * d.real if d.real else z.imag * d.imag):
        if rocks[rc] == "O":
            offset = 0
            while rc - offset - d in rocks and rocks[rc - offset - d] == ".":
                offset += d
            rocks[rc] = "."
            rocks[rc - offset] = "O"
    return frozenset(rocks.items())


def spin(rocks_set: frozenset[tuple[complex, str]]) -> frozenset[tuple[complex, str]]:
    for direction in (1, 1j, -1, -1j):
        rocks_set = tilt(rocks_set, direction)

    return rocks_set


def load(rocks_set: frozenset[tuple[complex, str]]) -> int:
    return sum(int(max_rows - rc.real) for rc, char in rocks_set if char == "O")


with open("../input/14.txt") as f:
    rocks_initial = frozenset(
        (r + c*1j, char)
        for r, row in enumerate(f)
        for c, char in enumerate(row.strip())
    )

max_rows = int(max((rc.real for rc, _ in rocks_initial))) + 1
print(load(tilt(rocks_initial, 1)))

spins = 0
spins_to_load = {}
rocks_to_spins = {}
rocks_set = rocks_initial
while rocks_set not in rocks_to_spins:
    spins += 1
    rocks_to_spins[rocks_set] = spins
    rocks_set = spin(rocks_set)
    spins_to_load[spins] = load(rocks_set)

spins = spins + 1
print(spins_to_load[rocks_to_spins[rocks_set] + (1_000_000_000 - spins) % (spins - rocks_to_spins[rocks_set])])
