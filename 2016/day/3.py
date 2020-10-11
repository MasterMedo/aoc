with open('../input/3.txt') as f:
    data = [list(map(int, args)) for args in map(str.split, f)]

print(sum(0 < sum(sides) - 2*max(sides) for sides in data))
print(sum(0 < sum(sides) - 2*max(sides)
          for three_by_three in zip(data[::3], data[1::3], data[2::3])
          for sides in zip(*three_by_three)))
