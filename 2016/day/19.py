with open('../input/19.txt') as f:
    n = int(f.read())

x = 1
while x < n:
    x *= 2

x /= 2
print(int((n - x) * 2 + 1))

x = 1
while x < n:
    x *= 3

x /= 3
print(int(n - x if n - x <= x else (n - 2*x)//2 + 1))
