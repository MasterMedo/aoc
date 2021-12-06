lanternfish = [0] * 9
with open("../input/6.txt") as f:
    for n in f.read().split(","):
        lanternfish[int(n)] += 1

for days_passed in range(256):
    fish = [lanternfish[i + 1] for i in range(8)] + [0]
    fish[6] += lanternfish[0]
    fish[8] += lanternfish[0]
    lanternfish = fish
    if days_passed == 79:
        print(sum(lanternfish))

print(sum(lanternfish))
