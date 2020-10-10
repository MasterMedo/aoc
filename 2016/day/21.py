from collections import deque

part2 = False

with open('../input/21.txt') as f:
    instructions = [line for line in f]

word = list('abcdefgh')
if part2:
    word = list('fbgdceah')
    instructions = reversed(instructions)

for line in instructions:
    cmd, obj, left, *_, right = line.split()
    if cmd == 'swap':
        if obj == 'position':
            i, j = int(left), int(right)

        elif obj == 'letter':
            i, j = [i for i, c in enumerate(word) if c in {left, right}]

        word[i], word[j] = word[j], word[i]

    elif cmd == 'reverse':
        left, right = sorted(map(int, [left, right]))
        if left:
            word = word[:left] + word[right:left-1:-1] + word[right+1:]
        else:
            word = word[right::-1] + word[right+1:]

    elif cmd == 'rotate':
        tmp = deque(word)
        if obj == 'based':
            for i, c in enumerate(word):
                if c == right:
                    break

            rotations = i + 1 + (i >= 4)
            if part2:
                rotations = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 8, 0: 1}[i]

        elif obj == 'left':
            rotations = -int(left)

        elif obj == 'right':
            rotations = int(left)

        if part2:
            rotations *= -1

        tmp.rotate(rotations)
        word = list(tmp)

    elif cmd == 'move':
        i, j = int(left), int(right)
        if part2:
            i, j = j, i

        c = word[i]
        del word[i]
        word.insert(j, c)

print(''.join(word))
