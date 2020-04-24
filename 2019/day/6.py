from collections import defaultdict

stars = defaultdict(set)
with open('../input/6.txt') as f:
    for line in f:
        parent, child = line[:-1].split(')')
        stars[parent].add(child)

tree = dict()
nodes = [['COM', tree]]
while nodes:
    name, root = nodes.pop()
    for star in stars[name]:
        root[star] = dict()
        nodes.append([star, root[star]])

nodes.append(tree)
count, level = 0, 1
santa = you = parent = 0
while any(nodes):
    for node in nodes:
        for child in node:
            count += level
            if child == 'SAN':
                santa = level

            if child == 'YOU':
                you = level

            subtree = str(node[child])
            if 'SAN' in subtree and 'YOU' in subtree:
                parent = level

    nodes = [node[child] for node in nodes for child in node]
    level += 1

print(count)
print(santa + you - 2*parent - 2)
