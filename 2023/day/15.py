from collections import defaultdict


def hash_algorithm(label: str) -> int:
    hash_sum = 0
    for char in label:
        hash_sum += ord(char)
        hash_sum *= 17
        hash_sum %= 256
    return hash_sum


with open("../input/15.txt") as f:
    labels = f.read().strip().split(",")

print(sum(hash_algorithm(label) for label in labels))

boxes = defaultdict(dict)
for i, instruction in enumerate(labels):
    if "-" in instruction:
        label = instruction[:-1]
        box = hash_algorithm(label)
        if label in boxes[box]:
            del boxes[box][label]
    else:
        label, focal_length = instruction.split("=")
        box = hash_algorithm(label)
        if label in boxes[box]:
            boxes[box][label][1] = int(focal_length)
        else:
            boxes[box][label] = [i, int(focal_length)]

focusing_power = 0
for box, lenses in boxes.items():
    for i, (_, focal_length) in enumerate(sorted(lenses.values())):
        focusing_power += (box + 1) * (i + 1) * focal_length

print(focusing_power)
