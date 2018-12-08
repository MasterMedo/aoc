def solve(child, meta):
    if child == 0:
        return [sum(next(data) for _ in range(meta))]*2
    children = {}
    total = value = 0
    for i in range(1, child+1):
        _total, _value = solve(next(data), next(data))
        total += _total
        children[i] = _value
    for _ in range(meta):
        _next = next(data)
        total += _next
        value += children.get(_next, 0)
    return total, value

data = iter(map(int, open('../input/8.txt').read().split()))

print(solve(next(data), next(data)))
