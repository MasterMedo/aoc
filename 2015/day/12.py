import json


def sum_(data, exclude=None, s=0):
    if isinstance(data, int):
        return data

    if isinstance(data, dict):
        if exclude in data.values():
            return 0
        s += sum(sum_(i, exclude) for i in data.values())

    if isinstance(data, (list, tuple)):
        s += sum(sum_(i, exclude) for i in data)

    return s


with open('../input/12.txt') as f:
    data = json.load(f)

print(sum_(data))
print(sum_(data, exclude='red'))
