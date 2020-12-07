import re


def contains(trait):
    traits = [t for t in data if trait in data[t]]
    return [trait, *[t for tr in traits for t in contains(tr)]]


def number(trait):
    return sum(data[trait][t] * (1 + number(t)) for t in data[trait])


data = {}
with open('../input/7.txt') as f:
    for line in f:
        trait = re.match(r'(\w+ \w+)', line)[0]
        inside = {t: int(n) for n, t in re.findall(r'(\d+) (\w+ \w+)', line)}
        data[trait] = inside

print(len(set(contains('shiny gold'))) - 1)
print(number('shiny gold'))
