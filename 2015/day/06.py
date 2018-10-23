x = [[0 for i in range(1000)] for i in range(1000)]

def toggle(a, b):
    global x
    for i in range(a[0], b[0]):
        for j in range(a[1], b[1]):
            #if x[i][j] == 1:
            #   x[i][j] = 0
            #else:
            #   x[i][j] = 1
            x[i][j] += 2
    return

def turn(n, a, b):
    global x
    for i in range(a[0], b[0]):
        for j in range(a[1], b[1]):
            #x[i][j] = n
            if x[i][j] >= 1 or n != -1:
                x[i][j] += n
    return

with open("../input/06.txt") as f:
    input = f.read().strip().splitlines()

for i in input:
    l = i.split() 
    a, b = l[-3].split(','), l[-1].split(',')
    a[0], a[1], b[0], b[1] = int(a[0]), int(a[1]), int(b[0])+1, int(b[1])+1
    if 'on' in i:
        turn(1, a, b) 
    elif 'off' in i:
        #turn(0, a, b)
        turn(-1, a, b)
    else:
        toggle(a, b)

print(sum([sum(i) for i in x]))
