from itertools import chain

f = open('../input/7.txt').readlines()
kids = dict((i.split()[0], i[:-1].replace('-> ', '').replace(',', '').split()[2:]) for i in f)
weight = dict((i.split()[0], int(i.split()[1].replace(')', '').replace('(', ''))) for i in f)

print set(kids).difference(set(chain(*kids.values()))).pop()

total = dict((kid, -float('inf')) for kid in kids)
while sum(total.values()) == -float('inf'):
    parent = kids.keys()[0]
    children = kids.pop(parent)
    above = [total[child] for child in children]
    total[parent] = weight[parent] + sum(above)
    if total[parent] == -float('inf'):
        kids[parent] = children
    elif len(above) and above.count(above[0]) != len(above):
        node = [x for x in children if above.count(total[x]) == 1].pop()
        print weight[node] + sum(set(above)) - 2 * total[node]
        break
