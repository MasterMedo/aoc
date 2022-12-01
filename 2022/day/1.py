with open("../input/1.txt") as f:
    elfs = [sum(map(int, elf.split("\n"))) for elf in f.read().split("\n\n")[:-1]]

print(max(elfs))
print(sum(list(sorted(elfs))[-3:]))
