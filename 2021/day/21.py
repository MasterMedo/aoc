from itertools import cycle
from functools import cache

with open("../input/21.txt") as f:
    player_1, player_2 = [int(line[-3:]) for line in f.readlines()]


def part_1(player_1, player_2, score_1=0, score_2=0, throws=0):
    if score_2 >= 1000:
        return score_1 * throws

    player_1 += sum(next(deterministic_die) for _ in range(3))
    player_1 = (player_1 - 1) % 10 + 1
    score_1 += player_1
    return part_1(player_2, player_1, score_2, score_1, throws + 3)


@cache
def part_2(player_1, player_2, score_1, score_2):
    if score_2 >= 21:
        return (0, 1)

    wins = [0, 0]
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                new_player_1 = (player_1 + i + j + k) % 10
                new_score_1 = score_1 + new_player_1 + 1
                win_2, win_1 = part_2(
                    player_2, new_player_1, score_2, new_score_1
                )
                wins[0] += win_1
                wins[1] += win_2

    return wins


deterministic_die = cycle(range(1, 101))
print(part_1(player_1, player_2))
print(max(part_2(player_1 - 1, player_2 - 1, 0, 0)))
