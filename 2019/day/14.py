from collections import defaultdict
from math import ceil
from re import findall


def ore_needed_for_n_fuel(n):
    ore = 0
    orders = defaultdict(int, {'FUEL': n})
    waste = defaultdict(int)
    while orders:
        chemical, amount_needed = orders.popitem()
        amount_produced, reactants = reactions[chemical]

        if waste[chemical] >= amount_needed:
            waste[chemical] -= amount_needed
        else:
            amount_needed = amount_needed - waste[chemical]
            waste[chemical] = 0
            reactions_needed = ceil(amount_needed/amount_produced)
            waste[chemical] += reactions_needed*amount_produced - amount_needed

            for reactant in reactants:
                if reactant == 'ORE':
                    ore += reactions_needed * reactants[reactant]
                else:
                    orders[reactant] += reactions_needed * reactants[reactant]
    return ore


reactions = dict()
with open('../input/14.txt') as f:
    for line in f.readlines():
        *reactants, product = [(name, int(amount)) for _, amount, name in
                               findall(r'((\d+) (\w+)[, =>]?)+', line)]
        reactions[product[0]] = (product[1], dict(reactants))

fuel = ore_needed_for_n_fuel(1)  # part2 do manual golden search over digits
print(fuel)
