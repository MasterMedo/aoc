from operator import mul
from itertools import count
from functools import reduce
from collections import deque

with open("../input/16.txt") as f:
    data = deque(str(bin(int(f.read()[:-1], 16)))[2:])


def parse():
    global version_sum
    version = int("".join(data.popleft() for _ in range(3)), 2)
    version_sum += version
    type_id = int("".join(data.popleft() for _ in range(3)), 2)
    if type_id == 4:  # literal value
        number = ""
        for i in count(1):
            first = data.popleft()
            number += "".join(data.popleft() for _ in range(4))
            if first == "0":
                break

        return int(number, 2), 6 + i * 5

    subpackets = []
    length_type_id = data.popleft()
    packet_length = 7

    if length_type_id == "1":
        total_subpackets = int("".join(data.popleft() for _ in range(11)), 2)
        packet_length += 11
        for i in range(total_subpackets):
            val, length = parse()
            subpackets.append(val)
            packet_length += length
    else:
        subpackets_length = int("".join(data.popleft() for _ in range(15)), 2)
        packet_length += 15
        while subpackets_length > 0:
            val, length = parse()
            subpackets.append(val)
            subpackets_length -= length
            packet_length += length

    if type_id == 0:  # sum
        val = sum(subpackets)
    if type_id == 1:  # product
        val = reduce(mul, subpackets)
    if type_id == 2:  # minimum
        val = min(subpackets)
    if type_id == 3:  # maximum
        val = max(subpackets)
    if type_id == 5:  # greater than
        val = subpackets[0] > subpackets[1]
    if type_id == 6:  # less than
        val = subpackets[0] < subpackets[1]
    if type_id == 7:  # equal to
        val = subpackets[0] == subpackets[1]

    return val, packet_length


version_sum = 0
val, _ = parse()
print(version_sum)
print(val)
