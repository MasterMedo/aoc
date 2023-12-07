from collections import Counter
from functools import partial


def score(order: str, j_as_joker: bool, hand: tuple[str, str]) -> tuple[str]:
    cards, _ = hand
    tally = []
    counter = Counter(cards)
    if j_as_joker:
        jokers = counter.get('J', 0)
        counter['J'] = 0
        counter[counter.most_common(1)[0][0]] += jokers
    match [n for n in counter.values() if n > 1]:
        case [5]:
            tally.append(7)
        case [4]:
            tally.append(6)
        case [2, 3] | [3, 2]:
            tally.append(5)
        case [3]:
            tally.append(4)
        case [2, 2]:
            tally.append(3)
        case [2]:
            tally.append(2)
        case []:
            tally.append(1)

    for card in cards:
        tally.append(order.index(card))

    return tally


ordering = "123456789TJQKA"
ordering2 = "J123456789TQKA"
with open("../input/7.txt") as f:
    hands = [line.split() for line in f]

hands.sort(key=partial(score, ordering, False))
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(hands)))
hands.sort(key=partial(score, ordering2, True))
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(hands)))
