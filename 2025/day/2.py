from math import log10, floor


def factors(n: int) -> list[int]:
    return [i for i in range(1, n + 1) if n % i == 0]


def nextInvalidPart1(n: int) -> int:
    def appendCandidate(base):
        if factor == 0:
            return
        candidate = 0
        cnt = 0
        for _ in range(digits // factor):
            candidate += base
            base *= 10**factor
            cnt += 1
        if cnt > 1 and candidate > n:
            candidates.append(candidate)
    digits = floor(log10(n)) + 1
    candidates = []
    if digits % 2 == 0:
        candidates.append(10**(digits+2) + 10**((digits+2)//2))
    else:
        return 10**(digits) + 10**((digits)//2)
    for factor in [digits//2]:
        base = n // 10**(digits - factor)
        appendCandidate(base)
        if floor(log10(n + 1)) + 1 == digits:
            appendCandidate(base + 1)
    return min(candidates)


def nextInvalidPart2(n: int) -> int:
    def appendCandidate(base):
        candidate = 0
        cnt = 0
        for _ in range(digits // factor):
            candidate += base
            base *= 10**factor
            cnt += 1
        if cnt > 1 and candidate > n:
            candidates.append(candidate)
    digits = floor(log10(n)) + 1
    candidates = []
    if digits % 2 == 0:
        candidates.append(sum(10**d for d in range(digits + 1)))
    else:
        candidates.append(10**digits + 10**(digits//2))
    for factor in factors(digits):
        base = n // 10**(digits - factor)
        appendCandidate(base)
        if floor(log10(n + 1)) + 1 == digits:
            appendCandidate(base + 1)
    return min(candidates)


def sumAllInvalid(numbers: list[tuple[int, int]], nextInvalid) -> int:
    s = 0
    for lo, hi in numbers:
        n = nextInvalid(lo-1)
        while n <= hi:
            s += n
            n = nextInvalid(n)
    return s


with open("../input/2.txt") as f:
    numbers = [tuple(map(int, x.split("-"))) for x in f.read().split(",")]

print(f"part1: {sumAllInvalid(numbers, nextInvalidPart1)}")
print(f"part2: {sumAllInvalid(numbers, nextInvalidPart2)}")
