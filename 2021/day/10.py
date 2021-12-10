with open("../input/10.txt") as f:
    data = f.readlines()

matching_parenthesis = {"(": ")", "[": "]", "{": "}", "<": ">"}
corrupted_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}

part_1 = 0
part_2 = []
for line in data:
    stack = []
    for c in line[:-1]:
        if c in ")]}>":
            if stack[-1] != c:
                part_1 += corrupted_score[c]
                break
            stack.pop()
        else:
            stack.append(matching_parenthesis[c])
    else:
        score = 0
        for c in reversed(stack):
            score = score * 5 + incomplete_score[c]
        part_2.append(score)

print(part_1)
print(list(sorted(part_2))[len(part_2) // 2])
