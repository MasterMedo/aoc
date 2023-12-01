import re

digits1 = {str(i): str(i) for i in range(1, 10)}
digits2 = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    **digits1,
}
sum1 = sum2 = 0
with open("../input/1.txt") as f:
    for line in f:
        digits = list(map(digits1.get, re.findall("|".join(digits1), line)))
        sum1 += int(digits[0] + digits[-1])
        digits = list(
            map(digits2.get, re.findall("(?=(" + "|".join(digits2) + "))", line))
        )
        sum2 += int(digits[0] + digits[-1])

print(sum1)
print(sum2)
