from collections import deque

def solve(players, last):
    circle = deque([0])
    scores = [0]*players
    for turn in xrange(1, last+1):
        player = (turn-1)%players
        if not turn % 23:
            circle.rotate(7)
            scores[player] += turn + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(turn)
    print max(scores)

players, last = (int(i) for i in open('../input/9.txt').read().split() if i.isdigit())
solve(players, last)
solve(players, last*100)
