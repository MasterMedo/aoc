from collections import defaultdict

bot = defaultdict(list)
output = defaultdict(list)
children = {}

with open('../input/10.txt') as f:
    for command, *args in map(str.split, f):
        if command == 'value':
            value, *_, index = args
            bot[int(index)].append(int(value))
        else:
            index, _, _, _, x, low, *_, y, high = args
            children[int(index)] = f'{x}[{low}]', f'{y}[{high}]'

while bot:
    for index, values in dict(bot).items():
        if len(values) == 2:
            low, high = sorted(bot.pop(index))
            lower, higher = children[index]
            eval(lower).append(low)
            eval(higher).append(high)
            if low == 17 and high == 61:
                print(index)

print(output[0][0] * output[1][0] * output[2][0])
