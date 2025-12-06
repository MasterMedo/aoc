with open("../input/5.ex") as f:
    healthy, ingredients = f.read().split("\n\n")

ranges = [tuple(map(int, line.split("-"))) for line in healthy.split("\n")]
compacted = []
while ranges:
    x, y = ranges.pop()
    for i in range(len(compacted)):
        a, b = compacted[i]
        if b < x or y < a:
            continue
        a, b = compacted.pop(i)
        ranges.append((min(a, x), max(b, y)))
        break
    else:
        compacted.append((x, y))


print(sum(any(lo <= int(ingredient) <= hi for lo, hi in compacted) for ingredient in ingredients.strip().split("\n")))
print(sum(hi - lo + 1 for lo, hi in compacted))
