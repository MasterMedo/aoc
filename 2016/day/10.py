from collections import defaultdict

bot = defaultdict(list)
output = defaultdict(list)

with open('../input/10.txt') as f:
    children = {}
    for line in map(str.split, f):
        if line[0] == 'value':
            bot[int(line[-1])].append(int(line[1]))
        else:
            children[int(line[1])] = line[ 5] +'['+ line[ 6] +']', \
                                     line[-2] +'['+ line[-1] +']'

while bot:
    for bot_n, v in dict(bot).iteritems():
        if len(v) == 2:
            v1, v2 = sorted(bot.pop(bot_n))
            lower, higher = children[bot_n]
            eval(lower).append(v1)
            eval(higher).append(v2)
            if v1 == 17 and v2 == 61:
                print(bot_n)

print output[0][0] * output[1][0] * output[2][0]
