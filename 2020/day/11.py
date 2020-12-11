import itertools as it  # noqa
from copy import deepcopy


def isvalid(row, col):
    return 0 <= row < ROWS and 0 <= col < COLUMNS


def neighbours1(r, c):
    return [(r-1, c-1), (r-1, c+1), (r, c-1), (r+1, c),
            (r+1, c+1), (r+1, c-1), (r, c+1), (r-1, c)]


def neighbours2(row, col):
    n = []
    for delta_r, delta_c in neighbours1(0, 0):
        for k in it.count(1):
            r = row + k * delta_r
            c = col + k * delta_c
            if isvalid(r, c):
                if data[r][c] != '.':
                    n.append((r, c))
                    break
            else:
                break
    return n


with open('../input/11.txt') as f:
    start = list(map(list, f.read().splitlines()))

ROWS, COLUMNS = len(start), len(start[0])

for neighbours, adjecent in [(neighbours1, 4), (neighbours2, 5)]:
    data = start
    for episode in it.count():
        data_ = deepcopy(data)
        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if seat == 'L' and all(data[x][y] != '#'
                                       for x, y in neighbours(i, j)
                                       if isvalid(x, y)):
                    data_[i][j] = '#'

                elif seat == '#' and sum(data[x][y] == '#'
                                         for x, y in neighbours(i, j)
                                         if isvalid(x, y)) >= adjecent:
                    data_[i][j] = 'L'

        if data == data_:
            print(sum(c == '#' for row in data_ for c in row))
            break

        data = data_
