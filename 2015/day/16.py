import re

with open('../input/16.txt') as f, open('../input/16tape.txt') as ftt:
    data = [{x[:3]: int(y) for x, y in re.findall(r'(\w+): (\d+)', line)}
            for line in f]
    tape = {x[:3]: int(y) for x, y in map(lambda l: l.split(': '), ftt)}

print(next(aunt+1 for aunt, test in enumerate(data)
            if all(tape[i] == test[i] for i in test)))

print(next(aunt+1 for aunt, test in enumerate(data)
            if all(i not in {'cat', 'tre', 'pom', 'gol'} and tape[i] == test[i]
                    or i in {'cat', 'tre'} and tape[i] < test[i]
                    or i in {'pom', 'gol'} and tape[i] > test[i]
                    for i in test)))
