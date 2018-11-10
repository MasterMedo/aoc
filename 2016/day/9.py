def out(string):
    i, n = 0, 0
    while True:
        if i >= len(string):
            break
        if string[i] == '(':
            end = string.index(')', i)
            x, y = map(int, string[i + 1:end].split('x'))
            # n += x*y - 1
            n += out(string[end + 1:end + 1 + x]) * y - 1
            i = end + x
        i += 1
        n += 1
    return n

with open('../input/9.txt') as f:
    data = f.read().strip()

print out(data)
