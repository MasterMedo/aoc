def solve(block):
    count, seen = 0, set()
    while not seen.intersection({tuple(block)}):
        count += 1
        seen.add(tuple(block))
        top = max(block)
        i = block.index(top)
        block[i] = 0
        for j in range(top):
            block[(i + j + 1) % len(block)] += 1
    print count
    return block

with open("../input/06.txt") as f:
    block = map(int, f.read().strip().split())

solve(solve(block))
