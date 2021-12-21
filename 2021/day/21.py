from itertools import cycle
from functools import cache

with open("../input/21.txt") as f:
    player_1, player_2 = [int(line[-3:]) for line in f.readlines()]


def deterministic_dice(player_1, player_2):
    score_a, score_b = 0, 0
    die = cycle(range(1, 101))
    throws = 0
    while True:
        player_1 += next(die) + next(die) + next(die)
        player_1 = (player_1 - 1) % 10 + 1
        score_a += player_1
        throws += 3
        if score_a >= 1000:
            return score_b * throws
        player_2 += next(die) + next(die) + next(die)
        player_2 = (player_2 - 1) % 10 + 1
        score_b += player_2
        throws += 3
        if score_b >= 1000:
            return score_a * throws


@cache
def quantum_dice(player_1, player_2, score_a, score_b):
    if score_b >= 21:
        return (0, 1)

    wins = [0, 0]
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                new_a = (player_1 + i + j + k) % 10
                win_b, win_a = quantum_dice(
                    player_2, new_a, score_b, score_a + new_a + 1
                )
                wins[0] += win_a
                wins[1] += win_b

    return wins


print(deterministic_dice(player_1, player_2))
print(max(quantum_dice(player_1 - 1, player_2 - 1, 0, 0)))
