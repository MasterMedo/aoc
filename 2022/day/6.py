def start_of(n: int) -> int:
    for i in range(n, len(data)):
        if len(set(data[i - n + 1 : i + 1])) == n:
            return i + 1


with open("../input/6.txt") as f:
    data = f.read().rstrip()

print(start_of(4))
print(start_of(14))
