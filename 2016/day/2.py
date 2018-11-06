def code(x, y, grid):
    for i in data:
        for j in i:
            if   j == 'R': x = min(x + 1,  (2 - abs(y))) # x = min(x + 1,  1))
            elif j == 'L': x = max(x - 1, -(2 - abs(y))) # x = max(x - 1, -1))
            elif j == 'U': y = min(y + 1,  (2 - abs(x))) # y = min(y + 1,  1))
            elif j == 'D': y = max(y - 1, -(2 - abs(x))) # y = max(y - 1, -1))
        print grid[x, y],

with open('../input/2.txt') as f:
    data = f.read().strip().splitlines()

#grid1 = {(-1, 1): 1, (0, 1): 2, (1, 1): 3, (-1, 0): 4, (0, 0): 0, (1, 0): 6, (-1, -1): 7, (0, -1): 8, (1, -1): 9}
grid2 = {(0, 2): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (-2, 0): 5, (-1, 0): 6, (0, 0): 7, (0, 1): 8, (2, 0): 9, (-1, -1): 'A', (0, -1): 'B', (1, -1): 'C', (0, -2): 'D'}
#code(0, 0, grid1)
code(-2, 0, grid2)
