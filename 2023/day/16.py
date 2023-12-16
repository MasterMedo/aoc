from collections import defaultdict


def energy(grid: dict[complex, str], start: tuple[complex, int]) -> int:
    seen = defaultdict(set)
    to_visit = [start]
    while to_visit:
        old_rc, d = to_visit.pop()
        rc = old_rc + d
        new_directions = []
        match grid[rc]:
            case "-":
                if d.imag:
                    new_directions.append(1)
                    new_directions.append(-1)
                else:
                    new_directions.append(d)
            case "|":
                if d.real:
                    new_directions.append(1j)
                    new_directions.append(-1j)
                else:
                    new_directions.append(d)
            case "/":
                new_directions.append({1: -1j, 1j: -1, -1: 1j, -1j: 1}[d])
            case "\\":
                new_directions.append({1: 1j, 1j: 1, -1: -1j, -1j: -1}[d])
            case ".":
                new_directions.append(d)

        for d in new_directions:
            if d in seen[rc]:
                continue

            seen[rc].add(d)
            if rc + d in grid:
                to_visit.append((rc, d))
    return len(seen)


with open("../input/16.txt") as f:
    grid = {
        r * 1j + c: char
        for r, row in enumerate(f)
        for c, char in enumerate(row.strip())
    }

print(energy(grid, (-1 + 0*1j, 1)))

max_row = int(max(rc.imag for rc in grid))
max_col = int(max(rc.real for rc in grid))
starts = [
    *((r*1j, 1) for r in range(max_row + 1)),
    *((r*1j + max_col, -1) for r in range(max_row + 1)),
    *((c, 1j) for c in range(max_col + 1)),
    *((c + max_row*1j, -1j) for c in range(max_col + 1)),
]
print(max(energy(grid, start) for start in starts))
