from operator import attrgetter
from copy import deepcopy

class group:
    def __init__(self, index, population, line):
        words  = line.split()
        tmp    = ' '.join(words[7:-11])[1:-1]
        tmp    = tmp.replace(',', '').split(';')
        if '' in tmp: tmp.remove('')
        traits = {t: tt for t, _, *tt in map(str.split, tmp)}

        self.id         = index
        self.population = population
        self.units      = int(words[0])
        self.hp         = int(words[4])
        self.dmgbase    = int(words[-6])
        self.dmgtype    = words[-5]
        self.initiative = int(words[-1])
        self.weak       = traits.get('weak', [])
        self.immune     = traits.get('immune', [])
        self.target     = ''

    @property
    def dmg(self):
        if self.population == 'Immune System':
            return boost + self.dmgbase
        return self.dmgbase

    @property
    def effpower(self):
        return self.units * self.dmg

    def __repr__(self):
        return str(vars(self))

    def damage(self, target):
        if self.dmgtype in target.immune: return 0
        if self.dmgtype in target.weak:   return 2 * self.effpower
        else:                             return self.effpower

    def attack(self):
        dmg = self.damage(self.target)
        self.target.defend(dmg)

    def defend(self, dmg):
        self.units = max(0, self.units - dmg // self.hp)

def game(groups):
    while len(set(g.population for g in groups)) > 1:
        attacked = set()
        multikey = attrgetter('effpower', 'initiative')
        for group in sorted(groups, key=multikey, reverse=True):
            enemies = filter(lambda g: g.population != group.population,
                            groups-attacked)
            multikey = lambda g: (group.damage(g), g.effpower, g.initiative)
            for target in sorted(enemies, key=multikey, reverse=True):
                if group.damage(target):
                    group.target = target
                    attacked.add(group.target)
                break
        if not len(attacked):
            break
        for group in sorted(groups, key=attrgetter('initiative'), reverse=True):
            if group in groups and group.target:
                group.attack()
                if not group.target.units:
                    groups.remove(group.target)
                group.target = ''
    return groups

done, boost, groups = 0, 0, set()
with open('../input/24.txt') as f:
    for _ in range(2):
        population = line if (line := next(f)[:-2]) else next(f)[:-2]
        while True:
            groups.add(group(len(groups)%10+1, population, next(f)))
            if not len(groups) % 10:
                break

while done < 2:
    result = game(deepcopy(groups))
    if not boost or not any('Infection' == g.population for g in result):
        print(sum(g.units for g in result))
        done += 1
    boost += 1
