from math import log10, floor


def battery(n, amount):
    arr = []
    for i in range(floor(log10(n)), -1, -1):
        digit, n = divmod(n, 10 ** i)
        arr.append(digit)
        if len(arr) <= amount:
            continue

        found = False
        for i in range(len(arr) - 1):
            if found:
                arr[i] = arr[i+1]
                continue
            elif arr[i] < arr[i+1]:
                found = True
                arr[i] = arr[i+1]

        if len(arr) > amount:
            del arr[-1]
    return sum(arr[i] * 10**(amount-i-1) for i in range(amount))


with open("../input/3.txt") as f:
    arr = [int(line) for line in f.readlines()]

print(f"part1: {sum(battery(n, 2) for n in arr)}")
print(f"part2: {sum(battery(n, 12) for n in arr)}")
