s1 = s2 = 0
with open('../input/2.txt') as f:
    for line in f:
        numbers, char, password = line.split()
        lo, hi = map(int, numbers.split('-'))
        char = char[0]
        if lo <= password.count(char) <= hi:
            s1 += 1

        if (password[lo-1] == char) ^ (password[hi-1] == char):
            s2 += 1

print(s1)
print(s2)
