from collections import defaultdict


def seat(name, names, n):
    if not names:
        return n + data[frozenset([name, starting_name])]

    return max(seat(name_, names - {name_}, n + data[frozenset([name, name_])])
               for name_ in names)


data = defaultdict(int)
with open('../input/13.txt') as f:
    for name, _, gain, n, *_, name_ in map(str.split, f.readlines()):
        data[frozenset([name, name_[:-1]])] += int(n) * (-1)**(gain != 'gain')

names = {name for name_pair in data for name in name_pair}
# names = names.union({'me'})

starting_name = names.pop()
print(seat(starting_name, names, 0))
