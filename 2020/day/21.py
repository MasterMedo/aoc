from collections import defaultdict

data = []
with open('../input/21.txt') as f:
    for line in f:
        i, a = line.split('(')
        data.append((i.split(), a[9:-2].split(', ')))

food = defaultdict(set)
for ingridients, allergens in data:
    for ingridient in ingridients:
        for allergen in allergens:
            food[allergen].add(ingridient)

for ingridients, allergens in data:
    for allergen in allergens:
        for ingridient in set(food[allergen]):
            if ingridient not in ingridients:
                food[allergen].remove(ingridient)

visit = {allergen for allergen in food if len(food[allergen]) == 1}
seen = set(visit)
while visit:
    allergen = visit.pop()
    ingridient = next(iter(food[allergen]))
    for a, i in food.items():
        if len(i) > 1:
            if ingridient in i:
                food[a].remove(ingridient)
                if len(food[a]) == 1:
                    visit.add(a)

toxic = set.union(*food.values())
d = dict((v.pop(), k) for k, v in food.items())

print(sum(ingridient not in toxic
          for ingridients, a in data
          for ingridient in ingridients))
print(','.join(sorted(d.keys(), key=lambda k: d[k])))
