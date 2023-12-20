from collections import defaultdict
from itertools import pairwise


def area(instructions: list[str], read_color: bool = False) -> int:
    grid = defaultdict(lambda: ".")
    xy = 0
    horizontal = {0}
    vertical = {0}
    moves = []
    for line in instructions:
        direction, steps, color = line.split()
        color = color.strip("(#)")
        steps = int(steps)
        if read_color:
            direction = "RDLU"[int(color[-1])]
            steps = int(color[:-1], 16)

        xy = xy + steps * {"U": -1j, "L": -1, "R": 1, "D": 1j}[direction]
        moves.append((direction, steps))
        horizontal.add(xy.real)
        horizontal.add(xy.real - 1)
        vertical.add(xy.imag)
        vertical.add(xy.imag - 1)

    horizontal = list(sorted(horizontal))
    vertical = list(sorted(vertical))
    ups = {down: up for up, down in pairwise(vertical)}
    downs = {up: down for up, down in pairwise(vertical)}
    lefts = {right: left for left, right in pairwise(horizontal)}
    rights = {left: right for left, right in pairwise(horizontal)}
    # This is a list of intersections of all lines that would be created if we
    # dug the infinitely left-right and up-down lines. Each intersection
    # represents the space above and to the left of it.
    grid = {x + y*1j: False for x in horizontal for y in vertical}

    xy = 0
    for direction, steps in moves:
        new_xy = xy + steps * {"U": -1j, "L": -1, "R": 1, "D": 1j}[direction]
        match direction:
            case "R":
                for x in horizontal:
                    if xy.real <= x <= new_xy.real:
                        grid[x + xy.imag * 1j] = True
            case "D":
                for y in vertical:
                    if xy.imag <= y <= new_xy.imag:
                        grid[y * 1j + xy.real] = True
            case "L":
                for x in reversed(horizontal):
                    if xy.real >= x >= new_xy.real:
                        grid[x + xy.imag * 1j] = True
            case "U":
                for y in reversed(vertical):
                    if xy.imag >= y >= new_xy.imag:
                        grid[y * 1j + xy.real] = True
        xy = new_xy

    # ASSUMPTION: Middle of the map is inside of the shape
    # This is false for the example, but true for my input.
    start = horizontal[len(horizontal)//2] + vertical[len(vertical)//2] * 1j
    to_visit = [start]
    while to_visit:
        xy = to_visit.pop()
        neighbours = []
        if xy.imag in ups:
            neighbours.append(xy.real + ups[xy.imag] * 1j)
        if xy.imag in downs:
            neighbours.append(xy.real + downs[xy.imag] * 1j)
        if xy.real in rights:
            neighbours.append(rights[xy.real] + xy.imag * 1j)
        if xy.real in lefts:
            neighbours.append(lefts[xy.real] + xy.imag * 1j)
        for new_xy in neighbours:
            if not grid[new_xy]:
                grid[new_xy] = True
                to_visit.append(new_xy)

    return sum(int((xy.real - lefts[xy.real]) * (xy.imag - ups[xy.imag])) for xy, dug in grid.items() if dug)


with open("../input/18.txt") as f:
    instructions = f.read().splitlines()

print(area(instructions))
print(area(instructions, True))
