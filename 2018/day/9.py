from collections import deque

def solve(players, last):
    circle = deque([0])
    scores = players*[0]
    for turn in range(1, last+1):
        player = (turn-1)%players
        if turn % 23 == 0:
            circle.rotate(-7)
            scores[player] += turn + circle.pop()
        else:
            circle.rotate(2)
            circle.append(turn)
    print max(scores)

players, last = (int(i) for i in open('../input/9.txt').read().split() if i.isdigit())
solve(players, last)
solve(players, last*100)
