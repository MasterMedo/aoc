with open('../input/4.txt') as f:
    x, y = map(int, f.read().split('-'))

counter = 0
for i in range(x, y+1):
    standalone = False
    password = str(i)
    digit = 0
    for j in range(len(password)-1):
        if password[j] > password[j+1]:
            break

        if password[j] == password[j+1]:
            digit += 1
        else:
            if digit == 1:
                standalone = True
            digit = 0

        # if digit: digit = 1 # uncomment for part1
    else:
        if standalone or digit == 1:
            counter += 1

print(counter)
