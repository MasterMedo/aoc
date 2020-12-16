from math import prod

with open('../input/16.txt') as f:
    fields, my_ticket, tickets = [chunk.split('\n')
                                  for chunk in f.read().strip().split('\n\n')]

rules = dict()
for line in fields:
    key, ranges = line.split(': ')
    rules[key] = [list(map(int, r.split('-'))) for r in ranges.split('or')]

my_ticket = list(map(int, my_ticket[1].split(',')))
tickets = [list(map(int, line.split(','))) for line in tickets[1:]]

error = 0
wrong = set()
for i, ticket in enumerate(tickets):
    for n in ticket:
        if all(lo > n or n > hi for rule in rules for lo, hi in rules[rule]):
            error += n
            wrong.add(i)

print(error)

columns = [set(rules.keys()) for _ in range(len(tickets[0]))]
for i, ticket in enumerate(tickets):
    if i not in wrong:
        for rule in rules:
            for j, n in enumerate(ticket):
                if a := all(n < lo or hi < n for lo, hi in rules[rule]):
                    columns[j] -= {rule}

columns_ = []
while columns_ != columns:
    columns_ = [set(column) for column in columns]
    for i, column in enumerate(columns):
        if len(column) == 1:
            for j, column2 in enumerate(columns):
                if i != j:
                    columns[j] -= column

columns = [next(iter(column)) for column in columns]
print(prod(n for c, n in zip(columns, my_ticket) if 'departure' in c))
