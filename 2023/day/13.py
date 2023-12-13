def count_mirrors(arr: list[str], ignore=-1) -> int:
    for i in range(len(arr) - 1):
        c = 0
        while i - c >= 0 and i + c + 1 < len(arr):
            if arr[i - c] != arr[i + c + 1]:
                break
            c += 1
        else:
            if i + 1 == ignore:
                continue
            return i + 1
    return 0


with open("../input/13.txt") as f:
    patterns = f.read().strip().split("\n\n")

horizontal_mirrors = 0
vertical_mirrors = 0
horizontal_mirrors2 = 0
vertical_mirrors2 = 0
for p, pattern in enumerate(patterns):
    rows = list(map(list, pattern.split("\n")))
    cols = list(zip(*rows))
    horizontal_count = count_mirrors(rows)
    vertical_count = count_mirrors(cols)
    horizontal_mirrors += horizontal_count
    vertical_mirrors += vertical_count
    matches = set()
    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            rows[r][c] = "#" if char == "." else "."
            cols = list(zip(*rows))
            horizontal_count2 = count_mirrors(rows, horizontal_count)
            vertical_count2 = count_mirrors(cols, vertical_count)
            if bool(horizontal_count2) ^ bool(vertical_count2):
                matches.add((horizontal_count2, vertical_count2))
            rows[r][c] = char
    a, b = matches.pop()
    horizontal_mirrors2 += a
    vertical_mirrors2 += b

print(100 * horizontal_mirrors + vertical_mirrors)
print(100 * horizontal_mirrors2 + vertical_mirrors2)
