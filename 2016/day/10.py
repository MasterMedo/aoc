from operator import mul

bots = {}
with open('../input/10.txt') as f:
    for i in (j.split() for j in sorted(f.readlines())):
        if i[0] == 'bot':
            bots['bot' + i[1]] = {'low': i[5] + i[6], 'high': i[-2] + i[-1], 'vals': []}
            if i[5] == 'output':
                bots[i[5] + i[6]] = {'vals': []}
            if i[-2] == 'output':
                bots[i[-2] + i[-1]] = {'vals': []}
        else:
            bots['bot' + i[-1]]['vals'].append(int(i[1]))
            if len(bots['bot' + i[-1]]['vals']) == 2:
                two_val_bots = {'bot' + i[-1]: bots['bot' + i[-1]]}

while len(two_val_bots):
    for bot in two_val_bots.keys():
        if len(bots[bots[bot]['high']]['vals']) == 2 \
        or len(bots[bots[bot]['high']]['vals']) == 2:
            continue

        cur = two_val_bots.pop(bot)
        cur['vals'] = sorted(cur['vals'])

        if set(cur['vals']) == {17, 61}:
            print bot

        for val in ['high', 'low']:
            bots[cur[val]]['vals'].append(cur['vals'].pop())
            if len(bots[cur[val]]['vals']) == 2:
                two_val_bots[cur[val]] = bots[cur[val]]
        
print reduce(mul, [bots['output0']['vals'].pop(), bots['output1']['vals'].pop(), bots['output2']['vals'].pop()])
