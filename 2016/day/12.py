from functools import lru_cache


@lru_cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 2 else 1


with open('../input/12.txt') as f:
    data = [[int(i) if i[-1].isdigit() else i for i in line[:-1].split()]
            for line in f]


print(fib(data[2][1]+2) + int(data[16][1]) * int(data[17][1]))
print(fib(data[2][1] + data[5][1] + 2) + data[16][1]*data[17][1])
