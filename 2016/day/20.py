with open('../input/20.txt') as f:
    ranges = list(sorted([list(map(int, line.split('-'))) for line in f]))

ip = 0
first = True
whitelist = []
for low, high in ranges:
    for i, (low_, high_) in enumerate(whitelist):
        if low_ < low < high_:
            whitelist[i][0] = low + 1

        if low_ < high < high_:
            whitelist[i][1] = high - 1

    if ip >= high:
        continue

    if ip >= low:
        ip = high + 1

    else:
        if first:
            print(ip)
            first = False

        whitelist.append([ip, low-1])
        ip = high + 1

print(sum(high - low + 1 for low, high in whitelist if low <= high))
