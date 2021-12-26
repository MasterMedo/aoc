from collections import defaultdict
from heapq import heappush, heappop


def solve(data, depth):
    state = defaultdict(set)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in "ABCD":
                state[c].add((x, y))

    state = tuple(z for c in "ABCD" for z in sorted(state[c]))
    rooms = {"A": 3, "B": 5, "C": 7, "D": 9}
    hallway = [1, 2, 4, 6, 8, 10, 11]
    seen = {state: 0}
    visit = list([(0, state)])
    while visit:
        _, state = heappop(visit)
        cost = seen[state]
        if state == tuple(
            (i, j) for i in range(3, 10, 2) for j in range(2, depth + 2)
        ):
            return cost

        positions = set(state)
        for i in range(len(state)):
            new = []
            c = "ABCD"[i // depth]
            x, y = state[i]
            if y != 1:  # amphipod is in a room
                if (x, y - 1) in positions:  # other amphipod is above him
                    continue

                if rooms[c] == x:  # amphipod is in the correct room
                    if all(
                        (x, y_) in positions
                        and c == "ABCD"[state.index((x, y_)) // depth]
                        for y_ in range(y + 1, depth + 2)
                    ):  # all amphipods below are in the correct room
                        continue  # amphipod shouldn't be moved

                left_hallway = hallway[hallway.index(x - 1) :: -1]
                right_hallway = hallway[hallway.index(x + 1) :]
                for hallway_ in (left_hallway, right_hallway):
                    for x_ in hallway_:
                        if (x_, 1) in positions:  # amphipod is blocked
                            break
                        new.append((x_, 1))

            else:  # amphipod is in the hallway
                skip = False  # if wrong amphipod in this amphipod's room
                for y_ in range(depth + 1, 1, -1):
                    if (rooms[c], y_) in positions:
                        c_ = "ABCD"[state.index((rooms[c], y_)) // depth]
                        if c_ != c:  # wrong amphipod in this amphipod's room
                            skip = True
                            break
                    else:  # sets `y_` to first available spot in room
                        break

                if skip:  # wrong amphipod in this amphipod's room
                    continue

                if x < rooms[c]:  # amphipod is left of his room
                    hallway_ = range(x + 1, rooms[c] + 1)
                else:  # amphipod is right of his room
                    hallway_ = range(x - 1, rooms[c] - 1, -1)

                for x_ in hallway_:
                    if (x_, 1) in positions:  # amphipod is blocked
                        break
                else:  # if path to amphipod's room is clear
                    new.append((x_, y_))

            L = i // depth * depth
            R = L + depth
            left = state[:L]
            right = state[R:]
            mid = state[L:R]
            for x_, y_ in new:
                my_amphipods = tuple(
                    sorted(
                        tuple(xy for xy in mid if xy != (x, y)) + ((x_, y_),)
                    )
                )
                state_ = left + my_amphipods + right
                move_cost = pow(10, "ABCD".index(c))
                new_cost = cost + (abs(x - x_) + abs(y - y_)) * move_cost
                if state_ not in seen or seen[state_] > new_cost:
                    seen[state_] = new_cost
                    heappush(visit, (new_cost, state_))


with open("../input/23.txt") as f:
    data = f.read().splitlines()

print(solve(data, depth=2))
data = data[:3] + ["  #D#C#B#A#", "  #D#B#A#C#"] + data[3:]
print(solve(data, depth=4))
