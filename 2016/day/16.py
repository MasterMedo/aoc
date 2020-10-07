disk_length = 272
# disk_length = 35651584

with open('../input/16.txt') as f:
    disk = list(f.read()[:-1])

while len(disk) < disk_length:
    disk += ['0'] + ['0' if i == '1' else '1' for i in reversed(disk)]

disk = disk[:disk_length]

while len(disk) % 2 == 0:
    new_disk = []
    for i, c in enumerate(disk[::2]):
        new_disk += '1' if c == disk[i*2 + 1] else '0'
    disk = new_disk

print(''.join(disk))
