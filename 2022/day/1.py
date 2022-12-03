with open("../input/1.txt") as f:
    elfs = [sum(map(int, elf.split())) for elf in f.read().split("\n\n")]

print(max(elfs))
print(sum(sorted(elfs, reverse=True)[:3]))
