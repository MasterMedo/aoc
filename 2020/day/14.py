import re
from itertools import product
from collections import defaultdict

mem1 = defaultdict(int)
mem2 = defaultdict(int)
with open('../input/14.txt') as f:
    for line in f:
        if line.startswith('mask'):
            mask = list(line[7:].strip())
        else:
            address, n = map(int, re.findall(r'\d+', line))
            n_b = list(format(n, 'b').zfill(36))
            address_b = list(format(address, 'b').zfill(36))

            x = ''.join(n_bit if mask_bit == 'X' else mask_bit
                        for mask_bit, n_bit in zip(mask, n_b))
            mem1[address] = int(x, base=2)

            for floating in map(iter, product('10', repeat=mask.count('X'))):
                x = ''.join(next(floating) if mask_bit == 'X' else
                            address_bit if mask_bit == '0' else '1'
                            for mask_bit, address_bit in zip(mask, address_b))
                mem2[int(x, base=2)] = n


print(sum(mem1.values()))
print(sum(mem2.values()))
