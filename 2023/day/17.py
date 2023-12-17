from collections import defaultdict
from heapq import heappop, heappush


def min_heat_loss(city_blocks: dict[complex, int], min_straight: int, max_straight: int) -> int:
    max_row = int(max(rc.imag for rc in city_blocks))
    max_col = int(max(rc.real for rc in city_blocks))

    to_visit = [(0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 1)]
    seen = defaultdict(lambda: float("inf"))
    while to_visit:
        heat_loss, straight, rc_real, rc_imag, d_real, d_imag = heappop(to_visit)
        rc = rc_imag * 1j + rc_real
        d = d_imag * 1j + d_real
        if rc == max_row * 1j + max_col and straight >= min_straight:
            return heat_loss
        directions = []
        if straight < max_straight:
            directions.append(d)
        if straight >= min_straight:
            directions.append(d * 1j)
            directions.append(d / 1j)

        for new_d in directions:
            new_rc = rc + new_d
            new_straight = straight + 1 if new_d == d else 1
            if new_rc in city_blocks:
                new_heat_loss = heat_loss + city_blocks[new_rc]
                if seen[new_rc, new_d, new_straight] > new_heat_loss:
                    seen[new_rc, new_d, new_straight] = new_heat_loss
                    heappush(to_visit, (new_heat_loss, new_straight, new_rc.real, new_rc.imag, new_d.real, new_d.imag))


with open("../input/17.txt") as f:
    city_blocks = {
        r*1j + c: int(char)
        for r, row in enumerate(f)
        for c, char in enumerate(row.strip())
    }

print(min_heat_loss(city_blocks, 1, 3))
print(min_heat_loss(city_blocks, 4, 10))
