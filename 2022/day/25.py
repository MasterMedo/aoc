def f(n):
    if n == 0:
        return []
    if (n % 5) == 0:
        return ["0"] + f(n // 5)
    if (n % 5) == 1:
        return ["1"] + f(n // 5)
    if (n % 5) == 2:
        return ["2"] + f(n // 5)
    if (n % 5) == 3:
        return ["="] + f((n + 2) // 5)
    if (n % 5) == 4:
        return ["-"] + f((n + 1) // 5)


ds = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
IN = open("../input/25.txt").read()
total = 0
for ln in IN.strip().split("\n"):
    N = 0
    for c in ln:
        N *= 5
        N += ds[c]

    total += N

print("".join(f(total)[::-1]))
