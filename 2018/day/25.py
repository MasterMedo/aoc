with open('../input/25.txt') as f:
    stars = [tuple(map(int, line.split(','))) for line in f]

distance = lambda x, y: sum(abs(i-j) for i, j in zip(x, y))

systems = []
for x in stars:
    constellation, constellations = [x], []
    for system in systems:
        if any(distance(x, y) <= 3 for y in system):
            constellation.extend(system)
        else:
            constellations.append(system)
    systems = constellations + [constellation]

print(len(systems))
