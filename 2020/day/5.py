seat_id = m = 0
seen = set()
with open('../input/5.txt') as f:
    for line in f.read().splitlines():
        row = int(''.join('01'[c == 'B'] for c in line[:-3]), base=2)
        col = int(''.join('01'[c == 'R'] for c in line[-3:]), base=2)
        seat_id = max(seat_id, row * 8 + col)
        m = max(m, row)
        seen.add((row, col))

print(seat_id)
print(next(x*8+y for x in range(1, m) for y in range(8) if (x, y) not in seen))
