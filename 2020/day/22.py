from collections import deque


def game(p1, p2, recurse=True):
    seen = set()
    while p1 and p2:
        t = (tuple(p1), tuple(p2))
        if t in seen:
            return p1, True

        seen.add(t)
        c1 = p1.popleft()
        c2 = p2.popleft()
        if recurse and c1 <= len(p1) and c2 <= len(p2):
            if game(deque(e for i, e in enumerate(p1) if i < c1),
                    deque(e for i, e in enumerate(p2) if i < c2))[1]:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])

        elif c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return (p1, True) if p1 else (p2, False)


with open('../input/22.txt') as f:
    p1, p2 = f.read().split('\n\n')
    p1 = deque(map(int, p1.splitlines()[1:]))
    p2 = deque(map(int, p2.splitlines()[1:]))


winner = game(deque(p1), deque(p2), recurse=False)[0]
print(sum(i*j for i, j in enumerate(reversed(winner), 1)))
winner = game(p1, p2)[0]
print(sum(i*j for i, j in enumerate(reversed(winner), 1)))
